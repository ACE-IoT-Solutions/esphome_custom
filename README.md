# Collection of custom components for the the ESPHome Framework
This repository hosts a collection of custom components we've developed to support our use cases for the ESPHome Platform.
You can extract any particular folder from the custom\_components directory into the custom\_components directory in the root of your ESPHome Environment.
Examples of ESPHome Device configs can be found in the Examples Directory

### cse7766agg
The CSE7766 Power metering chip can be found in various Smart Plug devices, the default driver for the CSE7766 in ESPHOME measures avereage values from between polling intervals, the cse7766agg component add additional aggregate values that are computed off of the raw samples before being averaged into the normal output. These can be helpful for monitoring things like inrush current or loads that are switched by SCRs or other solid state switching devices.

