.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/uwb/radio.c

.. _`uwb_radio_start`:

uwb_radio_start
===============

.. c:function:: int uwb_radio_start(struct uwb_pal *pal)

    request that the radio be started

    :param pal:
        the PAL making the request.
    :type pal: struct uwb_pal \*

.. _`uwb_radio_start.description`:

Description
-----------

If the radio is not already active, a suitable channel is selected
and beacons are started.

.. _`uwb_radio_stop`:

uwb_radio_stop
==============

.. c:function:: void uwb_radio_stop(struct uwb_pal *pal)

    request that the radio be stopped.

    :param pal:
        the PAL making the request.
    :type pal: struct uwb_pal \*

.. _`uwb_radio_stop.description`:

Description
-----------

Stops the radio if no other PAL is making use of it.

.. This file was automatic generated / don't edit.

