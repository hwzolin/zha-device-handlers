"""Third Reality vibration sensor devices."""

from typing import Final

from zigpy.quirks import CustomCluster
from zigpy.quirks.v2 import QuirkBuilder
from zigpy.quirks.v2.homeassistant import UnitOfTime
import zigpy.types as t
from zigpy.zcl.foundation import BaseAttributeDefs, ZCLAttributeDef


class ThirdRealityVibrationSensorCluster(CustomCluster):
    """Third Reality's plug private cluster."""

    cluster_id = 0xFFF1

    class AttributeDefs(BaseAttributeDefs):
        """Define the attributes of a private cluster."""

        cool_down_time: Final = ZCLAttributeDef(
            id=0x0004,
            type=t.uint16_t,
            is_manufacturer_specific=True,
        )

(
    QuirkBuilder("Third Reality, Inc", "3RVS01031Z")
    .replaces(ThirdRealityVibrationSensorCluster)
    .number(
        attribute_name=ThirdRealityVibrationSensorCluster.AttributeDefs.cool_down_time.name,
        min_value=0,
        max_value=7200,
        step=1,
        unit=UnitOfTime.SECONDS,
        cluster_id=ThirdRealityVibrationSensorCluster.cluster_id,
        translation_key="cool_down_time",
        fallback_name="Cool Down Time",
    )
    .add_to_registry()
)
