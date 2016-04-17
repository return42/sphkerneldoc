.. -*- coding: utf-8; mode: rst -*-

======
hdmi.h
======


.. _`hdmi_infoframe`:

union hdmi_infoframe
====================

.. c:type:: hdmi_infoframe

    overall union of all abstract infoframe representations


.. _`hdmi_infoframe.definition`:

Definition
----------

.. code-block:: c

  union hdmi_infoframe {
    struct hdmi_any_infoframe any;
    struct hdmi_avi_infoframe avi;
    struct hdmi_spd_infoframe spd;
    union hdmi_vendor_any_infoframe vendor;
    struct hdmi_audio_infoframe audio;
  };


.. _`hdmi_infoframe.members`:

Members
-------

:``any``:
    generic infoframe

:``avi``:
    avi infoframe

:``spd``:
    spd infoframe

:``vendor``:
    union of all vendor infoframes

:``audio``:
    audio infoframe




.. _`hdmi_infoframe.description`:

Description
-----------

This is used by the generic pack function. This works since all infoframes
have the same header which also indicates which type of infoframe should be
packed.

