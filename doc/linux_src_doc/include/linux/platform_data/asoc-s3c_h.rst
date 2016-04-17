.. -*- coding: utf-8; mode: rst -*-

==========
asoc-s3c.h
==========


.. _`s3c_audio_pdata`:

struct s3c_audio_pdata
======================

.. c:type:: s3c_audio_pdata

    common platform data for audio device drivers


.. _`s3c_audio_pdata.definition`:

Definition
----------

.. code-block:: c

  struct s3c_audio_pdata {
    int (* cfg_gpio) (struct platform_device *);
  };


.. _`s3c_audio_pdata.members`:

Members
-------

:``cfg_gpio``:
    Callback function to setup mux'ed pins in I2S/PCM/AC97 mode


