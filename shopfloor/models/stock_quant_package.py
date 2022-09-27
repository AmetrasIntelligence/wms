from odoo import _, api, exceptions, fields, models


class StockQuantPackage(models.Model):
    _inherit = "stock.quant.package"

    move_line_ids = fields.One2many(
        comodel_name="stock.move.line",
        inverse_name="package_id",
        readonly=True,
        help="Technical field. Move lines moving this package.",
    )

    @api.constrains("name")
    def _constrain_name_unique(self):
        for rec in self:
            if self.search_count([("name", "=", rec.name), ("id", "!=", rec.id)]):
                raise exceptions.UserError(_("Package name must be unique!"))

    def move_package_to_location(self, dest_location):
        """Create inventories to move a package to a different location
        It should be called when the package is - in real life - already in
        the destination. It creates an inventory to remove the package from
        the source location and a second inventory to place the package
        in the destination (to reflect the reality).
        The source location is the current location of the package.
        """
        quant_values = []
        # sudo and the key in context activate is_inventory_mode on quants
        quants = self.quant_ids.sudo().with_context(inventory_mode=True)
        for quant in quants:
            quantity = quant.quantity
            quant.inventory_quantity = 0
            quant_values.append(
                self._move_package_quant_move_values(quant, dest_location, quantity)
            )

        quant_model = self.env["stock.quant"].sudo().with_context(inventory_mode=True)
        quant_model.create(quant_values)

    def _move_package_quant_move_values(self, quant, location, quantity):
        return {
            "product_id": quant.product_id.id,
            "inventory_quantity": quantity,
            "location_id": location.id,
            "lot_id": quant.lot_id.id,
            "package_id": quant.package_id.id,
            "owner_id": quant.owner_id.id,
        }
