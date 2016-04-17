.. -*- coding: utf-8; mode: rst -*-

=============
hdaudio_ext.h
=============


.. _`hdac_ext_device`:

struct hdac_ext_device
======================

.. c:type:: hdac_ext_device

    HDAC Ext device


.. _`hdac_ext_device.definition`:

Definition
----------

.. code-block:: c

  struct hdac_ext_device {
    struct hdac_device hdac;
  };


.. _`hdac_ext_device.members`:

Members
-------

:``hdac``:
    hdac core device
    ``nid_list`` - the dai map which matches the dai-name with the nid
    ``map_cur_idx`` - the idx in use in dai_map
    ``ops`` - the hda codec ops common to all codec drivers
    ``pvt_data`` - private data, for asoc contains asoc codec object


