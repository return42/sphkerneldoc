
.. _aboutthisdoc:

===================
About this document
===================


.. _translations:

Translations
============

If you know of any translations for this document, or you are interested in translating it, please email me hjk@hansjkoch.de.


.. _preface:

Preface
=======

For many types of devices, creating a Linux kernel driver is overkill. All that is really needed is some way to handle an interrupt and provide access to the memory space of the
device. The logic of controlling the device does not necessarily have to be within the kernel, as the device does not need to take advantage of any of other resources that the
kernel provides. One such common class of devices that are like this are for industrial I/O cards.

To address this situation, the userspace I/O system (UIO) was designed. For typical industrial I/O cards, only a very small kernel module is needed. The main part of the driver
will run in user space. This simplifies development and reduces the risk of serious bugs within a kernel module.

Please note that UIO is not an universal driver interface. Devices that are already handled well by other kernel subsystems (like networking or serial or USB) are no candidates for
an UIO driver. Hardware that is ideally suited for an UIO driver fulfills all of the following:

-  The device has memory that can be mapped. The device can be controlled completely by writing to this memory.

-  The device usually generates interrupts.

-  The device does not fit into one of the standard kernel subsystems.


.. _thanks:

Acknowledgments
===============

I'd like to thank Thomas Gleixner and Benedikt Spranger of Linutronix, who have not only written most of the UIO code, but also helped greatly writing this HOWTO by giving me all
kinds of background information.


.. _feedback:

Feedback
========

Find something wrong with this document? (Or perhaps something right?) I would love to hear from you. Please email me at hjk@hansjkoch.de.
