import esphome.codegen as cg
from esphome.components import output
import esphome.config_validation as cv
from esphome.const import CONF_ID, CONF_PIN
from voluptuous import NotIn

from .. import (
    CONF_ARDUINO_PORT_EXPANDER_ID,
    ArduinoPortExpanderComponent,
    arduino_port_expander_ns,
)

ArduinoPortExpanderOutput = arduino_port_expander_ns.class_(
    "ArduinoPortExpanderOutput",
    output.FloatOutput,
    cg.Component
)

CONFIG_SCHEMA = output.FLOAT_OUTPUT_SCHEMA.extend(
    {
        cv.Required(CONF_ID): cv.declare_id(ArduinoPortExpanderOutput),
        cv.GenerateID(CONF_ARDUINO_PORT_EXPANDER_ID): cv.use_id(ArduinoPortExpanderComponent),
        cv.Required(CONF_PIN): cv.All(
            cv.int_range(min=0, max=21),
            NotIn([18], "A4 is used for I2C SDA"),
            NotIn([19], "A5 is used for I2C SCL"),
        ),

    }
).extend(cv.COMPONENT_SCHEMA)


async def to_code(config):
    parent = await cg.get_variable(config[CONF_ARDUINO_PORT_EXPANDER_ID])
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
    await output.register_output(var, config)
    cg.add(var.set_pin(config[CONF_PIN]))
    cg.add(var.set_parent(parent))
