.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-dvb-frontend:

===================
struct dvb_frontend
===================

*man struct dvb_frontend(9)*

*4.6.0-rc5*

Frontend structure to be used on drivers.


Synopsis
========

.. code-block:: c

    struct dvb_frontend {
      struct dvb_frontend_ops ops;
      struct dvb_adapter * dvb;
      void * demodulator_priv;
      void * tuner_priv;
      void * frontend_priv;
      void * sec_priv;
      void * analog_demod_priv;
      struct dtv_frontend_properties dtv_property_cache;
    #define DVB_FRONTEND_COMPONENT_TUNER 0
    #define DVB_FRONTEND_COMPONENT_DEMOD 1
      int (* callback) (void *adapter_priv, int component, int cmd, int arg);
      int id;
      unsigned int exit;
    };


Members
=======

ops
    embedded struct dvb_frontend_ops

dvb
    pointer to struct dvb_adapter

demodulator_priv
    demod private data

tuner_priv
    tuner private data

frontend_priv
    frontend private data

sec_priv
    SEC private data

analog_demod_priv
    Analog demod private data

dtv_property_cache
    embedded struct dtv_frontend_properties

callback
    callback function used on some drivers to call either the tuner or
    the demodulator.

id
    Frontend ID

exit
    Used to inform the DVB core that the frontend thread should exit
    (usually, means that the hardware got disconnected.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
