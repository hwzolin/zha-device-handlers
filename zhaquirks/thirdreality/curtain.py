"""Third Reality curtain devices."""

from typing import Final

from zigpy.quirks import CustomCluster
from zigpy.quirks.v2 import QuirkBuilder
import zigpy.types as t
from zigpy.zcl.foundation import BaseAttributeDefs, ZCLAttributeDef


class ThirdRealityCurtainCluster(CustomCluster):
    """Third Reality's curtain private cluster."""

    cluster_id = 0xFFF1

    class AttributeDefs(BaseAttributeDefs):
        """Define the attributes of a private cluster."""

        enable_disable_pir_remote: Final = ZCLAttributeDef(
            id=0x0000,
            type=t.uint8_t,
            is_manufacturer_specific=True,
        )

(
    QuirkBuilder("Third Reality, Inc", "3RSB015BZ")
    .replaces(ThirdRealityCurtainCluster)
    .switch(
        attribute_name=ThirdRealityCurtainCluster.AttributeDefs.enable_disable_pir_remote.name,
        cluster_id=ThirdRealityCurtainCluster.cluster_id,
        force_inverted = True,
        # on_value = 0,
        # off_value = 1,
        translation_key="enable_disable_pir_mode",
        fallback_name="Enable/Disable PIR Remote",
    )
    .add_to_registry()
)
