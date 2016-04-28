.. -*- coding: utf-8; mode: rst -*-

.. _i2c:

=======================
I2C and SMBus Subsystem
=======================

I\ :sup:`2`\ C (or without fancy typography, "I2C") is an acronym for
the "Inter-IC" bus, a simple bus protocol which is widely used where low
data rate communications suffice. Since it's also a licensed trademark,
some vendors use another name (such as "Two-Wire Interface", TWI) for
the same bus. I2C only needs two signals (SCL for clock, SDA for data),
conserving board real estate and minimizing signal quality issues. Most
I2C devices use seven bit addresses, and bus speeds of up to 400 kHz;
there's a high speed extension (3.4 MHz) that's not yet found wide use.
I2C is a multi-master bus; open drain signaling is used to arbitrate
between masters, as well as to handshake and to synchronize clocks from
slower clients.

The Linux I2C programming interfaces support only the master side of bus
interactions, not the slave side. The programming interface is
structured around two kinds of driver, and two kinds of device. An I2C
"Adapter Driver" abstracts the controller hardware; it binds to a
physical device (perhaps a PCI device or platform_device) and exposes a
``struct i2c_adapter`` representing each I2C bus segment it manages. On
each I2C bus segment will be I2C devices represented by a
``struct i2c_client``. Those devices will be bound to a
``struct i2c_driver``, which should follow the standard Linux driver
model. (At this writing, a legacy model is more widely used.) There are
functions to perform various I2C protocol operations; at this writing
all such functions are usable only from task context.

The System Management Bus (SMBus) is a sibling protocol. Most SMBus
systems are also I2C conformant. The electrical constraints are tighter
for SMBus, and it standardizes particular protocol messages and idioms.
Controllers that support I2C can also support most SMBus operations, but
SMBus controllers don't support all the protocol options that an I2C
controller will. There are functions to perform various SMBus protocol
operations, either using I2C primitives or by issuing SMBus commands to
i2c_adapter devices which don't support those I2C operations.


.. toctree::
    :maxdepth: 1

    API-struct-i2c-driver
    API-struct-i2c-client
    API-struct-i2c-board-info
    API-I2C-BOARD-INFO
    API-struct-i2c-algorithm
    API-struct-i2c-timings
    API-struct-i2c-bus-recovery-info
    API-struct-i2c-adapter-quirks
    API-i2c-check-quirks
    API-module-i2c-driver
    API-builtin-i2c-driver
    API-i2c-register-board-info
    API-i2c-verify-client
    API-i2c-lock-adapter
    API-i2c-unlock-adapter
    API-i2c-new-device
    API-i2c-unregister-device
    API-i2c-new-dummy
    API-i2c-verify-adapter
    API-i2c-add-adapter
    API-i2c-add-numbered-adapter
    API-i2c-del-adapter
    API-i2c-parse-fw-timings
    API-i2c-del-driver
    API-i2c-use-client
    API-i2c-release-client
    API---i2c-transfer
    API-i2c-transfer
    API-i2c-master-send
    API-i2c-master-recv
    API-i2c-smbus-read-byte
    API-i2c-smbus-write-byte
    API-i2c-smbus-read-byte-data
    API-i2c-smbus-write-byte-data
    API-i2c-smbus-read-word-data
    API-i2c-smbus-write-word-data
    API-i2c-smbus-read-block-data
    API-i2c-smbus-write-block-data
    API-i2c-smbus-xfer
    API-i2c-smbus-read-i2c-block-data-or-emulated




.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
