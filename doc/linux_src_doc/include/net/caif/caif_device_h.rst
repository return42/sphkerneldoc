.. -*- coding: utf-8; mode: rst -*-

=============
caif_device.h
=============


.. _`caif_dev_common`:

struct caif_dev_common
======================

.. c:type:: caif_dev_common

    data shared between CAIF drivers and stack.


.. _`caif_dev_common.definition`:

Definition
----------

.. code-block:: c

  struct caif_dev_common {
    void (* flowctrl) (struct net_device *net, int on);
    enum caif_link_selector link_select;
    int use_frag;
    int use_fcs;
    int use_stx;
  };


.. _`caif_dev_common.members`:

Members
-------

:``flowctrl``:
    Flow Control callback function. This function is
    supplied by CAIF Core Stack and is used by CAIF
    Link Layer to send flow-stop to CAIF Core.
    The flow information will be distributed to all
    clients of CAIF.

:``link_select``:
    Profile of device, either high-bandwidth or
    low-latency. This member is set by CAIF Link
    Layer Device in        order to indicate if this device
    is a high bandwidth or low latency device.

:``use_frag``:
    CAIF Frames may be fragmented.
    Is set by CAIF Link Layer in order to indicate if the
    interface receives fragmented frames that must be
    assembled by CAIF Core Layer.

:``use_fcs``:
    Indicate if Frame CheckSum (fcs) is used.
    Is set if the physical interface is
    using Frame Checksum on the CAIF Frames.

:``use_stx``:
    Indicate STart of frame eXtension (stx) in use.
    Is set if the CAIF Link Layer expects
    CAIF Frames to start with the STX byte.




.. _`caif_dev_common.description`:

Description
-----------

This structure is shared between the CAIF drivers and the CAIF stack.
It is used by the device to register its behavior.
CAIF Core layer must set the member flowctrl in order to supply
CAIF Link Layer with the flow control function.

