import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import sensor, uart
from esphome.const import CONF_CURRENT, CONF_ID, CONF_POWER, CONF_VOLTAGE, \
    UNIT_VOLT, ICON_FLASH, UNIT_AMPERE, UNIT_WATT

DEPENDENCIES = ['uart']

cse7766agg_ns = cg.esphome_ns.namespace('cse7766agg')
CSE7766AGGComponent = cse7766agg_ns.class_('CSE7766AGGComponent', cg.PollingComponent, uart.UARTDevice)

CONFIG_SCHEMA = cv.Schema({
    cv.GenerateID(): cv.declare_id(CSE7766AGGComponent),

    cv.Optional(CONF_VOLTAGE): sensor.sensor_schema(UNIT_VOLT, ICON_FLASH, 1),
    cv.Optional(CONF_CURRENT): sensor.sensor_schema(UNIT_AMPERE, ICON_FLASH, 2),
    cv.Optional('current_max'): sensor.sensor_schema(UNIT_AMPERE, ICON_FLASH, 2),
    cv.Optional('current_min'): sensor.sensor_schema(UNIT_AMPERE, ICON_FLASH, 2),
    cv.Optional(CONF_POWER): sensor.sensor_schema(UNIT_WATT, ICON_FLASH, 1),
}).extend(cv.polling_component_schema('60s')).extend(uart.UART_DEVICE_SCHEMA)


def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    yield cg.register_component(var, config)
    yield uart.register_uart_device(var, config)

    if CONF_VOLTAGE in config:
        conf = config[CONF_VOLTAGE]
        sens = yield sensor.new_sensor(conf)
        cg.add(var.set_voltage_sensor(sens))
    if CONF_CURRENT in config:
        conf = config[CONF_CURRENT]
        sens = yield sensor.new_sensor(conf)
        cg.add(var.set_current_sensor(sens))
    if CONF_POWER in config:
        conf = config[CONF_POWER]
        sens = yield sensor.new_sensor(conf)
        cg.add(var.set_power_sensor(sens))
    if 'current_max' in config:
        conf = config['current_max']
        sens = yield sensor.new_sensor(conf)
        cg.add(var.set_current_max_sensor(sens))
    if 'current_min' in config:
        conf = config['current_min']
        sens = yield sensor.new_sensor(conf)
        cg.add(var.set_current_min_sensor(sens))
