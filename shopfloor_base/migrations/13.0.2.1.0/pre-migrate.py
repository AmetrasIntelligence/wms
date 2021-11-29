from openupgradelib import openupgrade


@openupgrade.migrate()
def migrate(env, version):
    openupgrade.delete_records_safely_by_xml_id(
        env,
        [
            "shopfloor_base.group_shopfloor_manager",
            "shopfloor_base.group_shopfloor_user",
        ],
    )
