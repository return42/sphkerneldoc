
.. _otg:

===================
USB On-The-GO (OTG)
===================

USB OTG support on Linux 2.6 was initially developed by Texas Instruments for `OMAP <http://www.omap.com>`__ 16xx and 17xx series processors. Other OTG systems should work in
similar ways, but the hardware level details could be very different.

Systems need specialized hardware support to implement OTG, notably including a special *Mini-AB* jack and associated transceiver to support *Dual-Role* operation: they can act
either as a host, using the standard Linux-USB host side driver stack, or as a peripheral, using this "gadget" framework. To do that, the system software relies on small additions
to those programming interfaces, and on a new internal component (here called an "OTG Controller") affecting which driver stack connects to the OTG port. In each role, the system
can re-use the existing pool of hardware-neutral drivers, layered on top of the controller driver interfaces (*usb_bus* or *usb_gadget*). Such drivers need at most minor changes,
and most of the calls added to support OTG can also benefit non-OTG products.

-  Gadget drivers test the *is_otg* flag, and use it to determine whether or not to include an OTG descriptor in each of their configurations.

-  Gadget drivers may need changes to support the two new OTG protocols, exposed in new gadget attributes such as *b_hnp_enable* flag. HNP support should be reported through a
   user interface (two LEDs could suffice), and is triggered in some cases when the host suspends the peripheral. SRP support can be user-initiated just like remote wakeup,
   probably by pressing the same button.

-  On the host side, USB device drivers need to be taught to trigger HNP at appropriate moments, using ``usb_suspend_device()``. That also conserves battery power, which is useful
   even for non-OTG configurations.

-  Also on the host side, a driver must support the OTG "Targeted Peripheral List". That's just a whitelist, used to reject peripherals not supported with a given Linux OTG host.
   *This whitelist is product-specific; each product must modify ``otg_whitelist.h`` to match its interoperability specification.*

   Non-OTG Linux hosts, like PCs and workstations, normally have some solution for adding drivers, so that peripherals that aren't recognized can eventually be supported. That
   approach is unreasonable for consumer products that may never have their firmware upgraded, and where it's usually unrealistic to expect traditional PC/workstation/server kinds
   of support model to work. For example, it's often impractical to change device firmware once the product has been distributed, so driver bugs can't normally be fixed if they're
   found after shipment.

Additional changes are needed below those hardware-neutral *usb_bus* and *usb_gadget* driver interfaces; those aren't discussed here in any detail. Those affect the
hardware-specific code for each USB Host or Peripheral controller, and how the HCD initializes (since OTG can be active only on a single port). They also involve what may be called
an *OTG Controller Driver*, managing the OTG transceiver and the OTG state machine logic as well as much of the root hub behavior for the OTG port. The OTG controller driver needs
to activate and deactivate USB controllers depending on the relevant device role. Some related changes were needed inside usbcore, so that it can identify OTG-capable devices and
respond appropriately to HNP or SRP protocols.
