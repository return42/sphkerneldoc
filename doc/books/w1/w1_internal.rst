.. -*- coding: utf-8; mode: rst -*-

.. _w1_internal:

=============================
W1 API internal to the kernel
=============================


.. _w1_internal_api:

W1 API internal to the kernel
=============================


.. _w1.h:

drivers/w1/w1.h
---------------

W1 core functions.


.. toctree::
    :maxdepth: 1

    API-struct-w1-reg-num
    API-struct-w1-slave
    API-struct-w1-bus-master
    API-enum-w1-master-flags
    API-struct-w1-master
    API-struct-w1-async-cmd


.. _w1.c:

drivers/w1/w1.c
---------------

W1 core functions.


.. toctree::
    :maxdepth: 1

    API-w1-search
    API-w1-process-callbacks


.. _w1_family.h:

drivers/w1/w1_family.h
----------------------

Allows registering device family operations.


.. toctree::
    :maxdepth: 1

    API-struct-w1-family-ops
    API-struct-w1-family


.. _w1_family.c:

drivers/w1/w1_family.c
----------------------

Allows registering device family operations.


.. toctree::
    :maxdepth: 1

    API-w1-register-family
    API-w1-unregister-family


.. _w1_int.c:

drivers/w1/w1_int.c
-------------------

W1 internal initialization for master devices.


.. toctree::
    :maxdepth: 1

    API-w1-add-master-device
    API-w1-remove-master-device


.. _w1_netlink.h:

drivers/w1/w1_netlink.h
-----------------------

W1 external netlink API structures and commands.


.. toctree::
    :maxdepth: 1

    API-enum-w1-cn-msg-flags
    API-enum-w1-netlink-message-types
    API-struct-w1-netlink-msg
    API-enum-w1-commands
    API-struct-w1-netlink-cmd


.. _w1_io.c:

drivers/w1/w1_io.c
------------------

W1 input/output.


.. toctree::
    :maxdepth: 1

    API-w1-write-8
    API-w1-read-8
    API-w1-write-block
    API-w1-touch-block
    API-w1-read-block
    API-w1-reset-bus
    API-w1-reset-select-slave
    API-w1-reset-resume-command
    API-w1-next-pullup
    API-w1-touch-bit
    API-w1-write-bit
    API-w1-pre-write
    API-w1-post-write
    API-w1-read-bit
    API-w1-triplet




.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
