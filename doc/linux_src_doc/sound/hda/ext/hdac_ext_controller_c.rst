.. -*- coding: utf-8; mode: rst -*-

=====================
hdac_ext_controller.c
=====================


.. _`snd_hdac_ext_bus_parse_capabilities`:

snd_hdac_ext_bus_parse_capabilities
===================================

.. c:function:: int snd_hdac_ext_bus_parse_capabilities (struct hdac_ext_bus *ebus)

    parse capablity structure

    :param struct hdac_ext_bus \*ebus:
        the pointer to extended bus object



.. _`snd_hdac_ext_bus_parse_capabilities.description`:

Description
-----------

Returns 0 if successful, or a negative error code.



.. _`snd_hdac_ext_bus_ppcap_enable`:

snd_hdac_ext_bus_ppcap_enable
=============================

.. c:function:: void snd_hdac_ext_bus_ppcap_enable (struct hdac_ext_bus *ebus, bool enable)

    enable/disable processing pipe capability

    :param struct hdac_ext_bus \*ebus:
        HD-audio extended core bus

    :param bool enable:
        flag to turn on/off the capability



.. _`snd_hdac_ext_bus_ppcap_int_enable`:

snd_hdac_ext_bus_ppcap_int_enable
=================================

.. c:function:: void snd_hdac_ext_bus_ppcap_int_enable (struct hdac_ext_bus *ebus, bool enable)

    ppcap interrupt enable/disable

    :param struct hdac_ext_bus \*ebus:
        HD-audio extended core bus

    :param bool enable:
        flag to enable/disable interrupt



.. _`snd_hdac_ext_bus_get_ml_capabilities`:

snd_hdac_ext_bus_get_ml_capabilities
====================================

.. c:function:: int snd_hdac_ext_bus_get_ml_capabilities (struct hdac_ext_bus *ebus)

    get multilink capability

    :param struct hdac_ext_bus \*ebus:
        HD-audio extended core bus



.. _`snd_hdac_ext_bus_get_ml_capabilities.description`:

Description
-----------

This will parse all links and read the mlink capabilities and add them
in hlink_list of extended hdac bus



.. _`snd_hdac_ext_bus_get_ml_capabilities.note`:

Note
----

this will be freed on bus exit by driver



.. _`snd_hdac_link_free_all`:

snd_hdac_link_free_all
======================

.. c:function:: void snd_hdac_link_free_all (struct hdac_ext_bus *ebus)

    free hdac extended link objects

    :param struct hdac_ext_bus \*ebus:
        HD-audio ext core bus



.. _`snd_hdac_ext_bus_get_link`:

snd_hdac_ext_bus_get_link
=========================

.. c:function:: struct hdac_ext_link *snd_hdac_ext_bus_get_link (struct hdac_ext_bus *ebus, const char *codec_name)

    get link based on codec name

    :param struct hdac_ext_bus \*ebus:
        HD-audio extended core bus

    :param const char \*codec_name:
        codec name



.. _`snd_hdac_ext_bus_link_power_up`:

snd_hdac_ext_bus_link_power_up
==============================

.. c:function:: int snd_hdac_ext_bus_link_power_up (struct hdac_ext_link *link)

    power up hda link

    :param struct hdac_ext_link \*link:
        HD-audio extended link



.. _`snd_hdac_ext_bus_link_power_down`:

snd_hdac_ext_bus_link_power_down
================================

.. c:function:: int snd_hdac_ext_bus_link_power_down (struct hdac_ext_link *link)

    power down hda link

    :param struct hdac_ext_link \*link:
        HD-audio extended link



.. _`snd_hdac_ext_bus_link_power_up_all`:

snd_hdac_ext_bus_link_power_up_all
==================================

.. c:function:: int snd_hdac_ext_bus_link_power_up_all (struct hdac_ext_bus *ebus)

    power up all hda link

    :param struct hdac_ext_bus \*ebus:
        HD-audio extended bus



.. _`snd_hdac_ext_bus_link_power_down_all`:

snd_hdac_ext_bus_link_power_down_all
====================================

.. c:function:: int snd_hdac_ext_bus_link_power_down_all (struct hdac_ext_bus *ebus)

    power down all hda link

    :param struct hdac_ext_bus \*ebus:
        HD-audio extended bus

