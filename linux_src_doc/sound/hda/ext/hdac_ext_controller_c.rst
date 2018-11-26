.. -*- coding: utf-8; mode: rst -*-
.. src-file: sound/hda/ext/hdac_ext_controller.c

.. _`snd_hdac_ext_bus_ppcap_enable`:

snd_hdac_ext_bus_ppcap_enable
=============================

.. c:function:: void snd_hdac_ext_bus_ppcap_enable(struct hdac_bus *bus, bool enable)

    enable/disable processing pipe capability

    :param bus:
        *undescribed*
    :type bus: struct hdac_bus \*

    :param enable:
        flag to turn on/off the capability
    :type enable: bool

.. _`snd_hdac_ext_bus_ppcap_int_enable`:

snd_hdac_ext_bus_ppcap_int_enable
=================================

.. c:function:: void snd_hdac_ext_bus_ppcap_int_enable(struct hdac_bus *bus, bool enable)

    ppcap interrupt enable/disable

    :param bus:
        *undescribed*
    :type bus: struct hdac_bus \*

    :param enable:
        flag to enable/disable interrupt
    :type enable: bool

.. _`snd_hdac_ext_bus_get_ml_capabilities`:

snd_hdac_ext_bus_get_ml_capabilities
====================================

.. c:function:: int snd_hdac_ext_bus_get_ml_capabilities(struct hdac_bus *bus)

    get multilink capability

    :param bus:
        *undescribed*
    :type bus: struct hdac_bus \*

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

.. c:function:: void snd_hdac_link_free_all(struct hdac_bus *bus)

    free hdac extended link objects

    :param bus:
        *undescribed*
    :type bus: struct hdac_bus \*

.. _`snd_hdac_ext_bus_get_link`:

snd_hdac_ext_bus_get_link
=========================

.. c:function:: struct hdac_ext_link *snd_hdac_ext_bus_get_link(struct hdac_bus *bus, const char *codec_name)

    get link based on codec name

    :param bus:
        *undescribed*
    :type bus: struct hdac_bus \*

    :param codec_name:
        codec name
    :type codec_name: const char \*

.. _`snd_hdac_ext_bus_link_power_up`:

snd_hdac_ext_bus_link_power_up
==============================

.. c:function:: int snd_hdac_ext_bus_link_power_up(struct hdac_ext_link *link)

    power up hda link

    :param link:
        HD-audio extended link
    :type link: struct hdac_ext_link \*

.. _`snd_hdac_ext_bus_link_power_down`:

snd_hdac_ext_bus_link_power_down
================================

.. c:function:: int snd_hdac_ext_bus_link_power_down(struct hdac_ext_link *link)

    power down hda link

    :param link:
        HD-audio extended link
    :type link: struct hdac_ext_link \*

.. _`snd_hdac_ext_bus_link_power_up_all`:

snd_hdac_ext_bus_link_power_up_all
==================================

.. c:function:: int snd_hdac_ext_bus_link_power_up_all(struct hdac_bus *bus)

    power up all hda link

    :param bus:
        *undescribed*
    :type bus: struct hdac_bus \*

.. _`snd_hdac_ext_bus_link_power_down_all`:

snd_hdac_ext_bus_link_power_down_all
====================================

.. c:function:: int snd_hdac_ext_bus_link_power_down_all(struct hdac_bus *bus)

    power down all hda link

    :param bus:
        *undescribed*
    :type bus: struct hdac_bus \*

.. This file was automatic generated / don't edit.

