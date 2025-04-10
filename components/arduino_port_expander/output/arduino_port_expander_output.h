#pragma once

#include "../arduino_port_expander.h"
#include "esphome/components/output/float_output.h"

namespace esphome {
namespace arduino_port_expander {

class ArduinoPortExpanderOutput : public output::FloatOutput, public Component {
 public:
  void set_parent(ArduinoPortExpanderComponent *parent) { this->parent_ = parent; }
  void set_pin(uint8_t pin) { this->pin_ = pin; };

 protected:
  void write_state(float state) override;

  ArduinoPortExpanderComponent *parent_;
  uint8_t pin_;
};

}  // namespace arduino_port_expander
}  // namespace esphome
