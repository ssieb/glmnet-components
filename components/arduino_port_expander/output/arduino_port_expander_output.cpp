#include "arduino_port_expander_output.h"

namespace esphome {
namespace arduino_port_expander {

void ArduinoPortExpanderOutput::write_state(float state) {
  this->parent_->analog_write(this->pin_, state * 255);
}

}  // namespace arduino_port_expander
}  // namespace esphome
