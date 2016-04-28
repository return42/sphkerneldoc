.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-dvb-frontend-ops:

=======================
struct dvb_frontend_ops
=======================

*man struct dvb_frontend_ops(9)*

*4.6.0-rc5*

Demodulation information and callbacks for ditialt TV


Synopsis
========

.. code-block:: c

    struct dvb_frontend_ops {
      struct dvb_frontend_info info;
      u8 delsys[MAX_DELSYS];
      void (* release) (struct dvb_frontend* fe);
      void (* release_sec) (struct dvb_frontend* fe);
      int (* init) (struct dvb_frontend* fe);
      int (* sleep) (struct dvb_frontend* fe);
      int (* write) (struct dvb_frontend* fe, const u8 buf[], int len);
      int (* tune) (struct dvb_frontend* fe,bool re_tune,unsigned int mode_flags,unsigned int *delay,enum fe_status *status);
      enum dvbfe_algo (* get_frontend_algo) (struct dvb_frontend *fe);
      int (* set_frontend) (struct dvb_frontend *fe);
      int (* get_tune_settings) (struct dvb_frontend* fe, struct dvb_frontend_tune_settings* settings);
      int (* get_frontend) (struct dvb_frontend *fe,struct dtv_frontend_properties *props);
      int (* read_status) (struct dvb_frontend *fe, enum fe_status *status);
      int (* read_ber) (struct dvb_frontend* fe, u32* ber);
      int (* read_signal_strength) (struct dvb_frontend* fe, u16* strength);
      int (* read_snr) (struct dvb_frontend* fe, u16* snr);
      int (* read_ucblocks) (struct dvb_frontend* fe, u32* ucblocks);
      int (* diseqc_reset_overload) (struct dvb_frontend* fe);
      int (* diseqc_send_master_cmd) (struct dvb_frontend* fe, struct dvb_diseqc_master_cmd* cmd);
      int (* diseqc_recv_slave_reply) (struct dvb_frontend* fe, struct dvb_diseqc_slave_reply* reply);
      int (* diseqc_send_burst) (struct dvb_frontend *fe,enum fe_sec_mini_cmd minicmd);
      int (* set_tone) (struct dvb_frontend *fe, enum fe_sec_tone_mode tone);
      int (* set_voltage) (struct dvb_frontend *fe,enum fe_sec_voltage voltage);
      int (* enable_high_lnb_voltage) (struct dvb_frontend* fe, long arg);
      int (* dishnetwork_send_legacy_command) (struct dvb_frontend* fe, unsigned long cmd);
      int (* i2c_gate_ctrl) (struct dvb_frontend* fe, int enable);
      int (* ts_bus_ctrl) (struct dvb_frontend* fe, int acquire);
      int (* set_lna) (struct dvb_frontend *);
      enum dvbfe_search (* search) (struct dvb_frontend *fe);
      struct dvb_tuner_ops tuner_ops;
      struct analog_demod_ops analog_ops;
      int (* set_property) (struct dvb_frontend* fe, struct dtv_property* tvp);
      int (* get_property) (struct dvb_frontend* fe, struct dtv_property* tvp);
    };


Members
=======

info
    embedded struct dvb_tuner_info with tuner properties

delsys[MAX_DELSYS]
    Delivery systems supported by the frontend

release
    callback function called when frontend is dettached. drivers should
    free any allocated memory.

release_sec
    callback function requesting that the Satelite Equipment Control
    (SEC) driver to release and free any memory allocated by the driver.

init
    callback function used to initialize the tuner device.

sleep
    callback function used to put the tuner to sleep.

write
    callback function used by some demod legacy drivers to allow other
    drivers to write data into their registers. Should not be used on
    new drivers.

tune
    callback function used by demod drivers that use ``DVBFE_ALGO_HW``;
    to tune into a frequency.

get_frontend_algo
    returns the desired hardware algorithm.

set_frontend
    callback function used to inform the demod to set the parameters for
    demodulating a digital TV channel. The properties to be used are
    stored at ``dvb_frontend``.dtv_property_cache;. The demod can
    change the parameters to reflect the changes needed for the channel
    to be decoded, and update statistics.

get_tune_settings
    callback function

get_frontend
    callback function used to inform the parameters actuall in use. The
    properties to be used are stored at
    ``dvb_frontend``.dtv_property_cache; and update statistics. Please
    notice that it should not return an error code if the statistics are
    not available because the demog is not locked.

read_status
    returns the locking status of the frontend.

read_ber
    legacy callback function to return the bit error rate. Newer drivers
    should provide such info via DVBv5 API, e. g.
    ``set_frontend``;/\ ``get_frontend``;, implementing this callback
    only if DVBv3 API compatibility is wanted.

read_signal_strength
    legacy callback function to return the signal strength. Newer
    drivers should provide such info via DVBv5 API, e. g.
    ``set_frontend``;/\ ``get_frontend``;, implementing this callback
    only if DVBv3 API compatibility is wanted.

read_snr
    legacy callback function to return the Signal/Noise rate. Newer
    drivers should provide such info via DVBv5 API, e. g.
    ``set_frontend``;/\ ``get_frontend``;, implementing this callback
    only if DVBv3 API compatibility is wanted.

read_ucblocks
    legacy callback function to return the Uncorrected Error Blocks.
    Newer drivers should provide such info via DVBv5 API, e. g.
    ``set_frontend``;/\ ``get_frontend``;, implementing this callback
    only if DVBv3 API compatibility is wanted.

diseqc_reset_overload
    callback function to implement the FE_DISEQC_RESET_OVERLOAD ioctl
    (only Satellite)

diseqc_send_master_cmd
    callback function to implement the FE_DISEQC_SEND_MASTER_CMD
    ioctl (only Satellite).

diseqc_recv_slave_reply
    callback function to implement the FE_DISEQC_RECV_SLAVE_REPLY
    ioctl (only Satellite)

diseqc_send_burst
    callback function to implement the FE_DISEQC_SEND_BURST ioctl
    (only Satellite).

set_tone
    callback function to implement the FE_SET_TONE ioctl (only
    Satellite).

set_voltage
    callback function to implement the FE_SET_VOLTAGE ioctl (only
    Satellite).

enable_high_lnb_voltage
    callback function to implement the FE_ENABLE_HIGH_LNB_VOLTAGE
    ioctl (only Satellite).

dishnetwork_send_legacy_command
    callback function to implement the
    FE_DISHNETWORK_SEND_LEGACY_CMD ioctl (only Satellite). Drivers
    should not use this, except when the DVB core emulation fails to
    provide proper support (e.g. if ``set_voltage`` takes more than 8ms
    to work), and when backward compatibility with this legacy API is
    required.

i2c_gate_ctrl
    controls the I2C gate. Newer drivers should use I2C mux support
    instead.

ts_bus_ctrl
    callback function used to take control of the TS bus.

set_lna
    callback function to power on/off/auto the LNA.

search
    callback function used on some custom algo search algos.

tuner_ops
    pointer to struct dvb_tuner_ops

analog_ops
    pointer to struct analog_demod_ops

set_property
    callback function to allow the frontend to validade incoming
    properties. Should not be used on new drivers.

get_property
    callback function to allow the frontend to override outcoming
    properties. Should not be used on new drivers.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
