.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-dvb-tuner-ops:

====================
struct dvb_tuner_ops
====================

*man struct dvb_tuner_ops(9)*

*4.6.0-rc5*

Tuner information and callbacks


Synopsis
========

.. code-block:: c

    struct dvb_tuner_ops {
      struct dvb_tuner_info info;
      int (* release) (struct dvb_frontend *fe);
      int (* init) (struct dvb_frontend *fe);
      int (* sleep) (struct dvb_frontend *fe);
      int (* suspend) (struct dvb_frontend *fe);
      int (* resume) (struct dvb_frontend *fe);
      int (* set_params) (struct dvb_frontend *fe);
      int (* set_analog_params) (struct dvb_frontend *fe, struct analog_parameters *p);
      int (* set_config) (struct dvb_frontend *fe, void *priv_cfg);
      int (* get_frequency) (struct dvb_frontend *fe, u32 *frequency);
      int (* get_bandwidth) (struct dvb_frontend *fe, u32 *bandwidth);
      int (* get_if_frequency) (struct dvb_frontend *fe, u32 *frequency);
    #define TUNER_STATUS_LOCKED 1
    #define TUNER_STATUS_STEREO 2
      int (* get_status) (struct dvb_frontend *fe, u32 *status);
      int (* get_rf_strength) (struct dvb_frontend *fe, u16 *strength);
      int (* get_afc) (struct dvb_frontend *fe, s32 *afc);
      int (* calc_regs) (struct dvb_frontend *fe, u8 *buf, int buf_len);
      int (* set_frequency) (struct dvb_frontend *fe, u32 frequency);
      int (* set_bandwidth) (struct dvb_frontend *fe, u32 bandwidth);
    };


Members
=======

info
    embedded struct dvb_tuner_info with tuner properties

release
    callback function called when frontend is dettached. drivers should
    free any allocated memory.

init
    callback function used to initialize the tuner device.

sleep
    callback function used to put the tuner to sleep.

suspend
    callback function used to inform that the Kernel will suspend.

resume
    callback function used to inform that the Kernel is resuming from
    suspend.

set_params
    callback function used to inform the tuner to tune into a digital TV
    channel. The properties to be used are stored at
    ``dvb_frontend``.dtv_property_cache;. The tuner demod can change
    the parameters to reflect the changes needed for the channel to be
    tuned, and update statistics. This is the recommended way to set the
    tuner parameters and should be used on newer drivers.

set_analog_params
    callback function used to tune into an analog TV channel on hybrid
    tuners. It passes ``analog_parameters``; to the driver.

set_config
    callback function used to send some tuner-specific parameters.

get_frequency
    get the actual tuned frequency

get_bandwidth
    get the bandwitdh used by the low pass filters

get_if_frequency
    get the Intermediate Frequency, in Hz. For baseband, should return
    0.

get_status
    returns the frontend lock status

get_rf_strength
    returns the RF signal strengh. Used mostly to support analog TV and
    radio. Digital TV should report, instead, via DVBv5 API
    (``dvb_frontend``.dtv_property_cache;).

get_afc
    Used only by analog TV core. Reports the frequency drift due to AFC.

calc_regs
    callback function used to pass register data settings for simple
    tuners. Shouldn't be used on newer drivers.

set_frequency
    Set a new frequency. Shouldn't be used on newer drivers.

set_bandwidth
    Set a new frequency. Shouldn't be used on newer drivers.


NOTE
====

frequencies used on get_frequency and set_frequency are in Hz for
terrestrial/cable or kHz for satellite.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
