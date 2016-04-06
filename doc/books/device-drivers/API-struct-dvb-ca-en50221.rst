
.. _API-struct-dvb-ca-en50221:

=====================
struct dvb_ca_en50221
=====================

*man struct dvb_ca_en50221(9)*

*4.6.0-rc1*

Structure describing a CA interface


Synopsis
========

.. code-block:: c

    struct dvb_ca_en50221 {
      struct module * owner;
      int (* read_attribute_mem) (struct dvb_ca_en50221 *ca,int slot, int address);
      int (* write_attribute_mem) (struct dvb_ca_en50221 *ca,int slot, int address, u8 value);
      int (* read_cam_control) (struct dvb_ca_en50221 *ca,int slot, u8 address);
      int (* write_cam_control) (struct dvb_ca_en50221 *ca,int slot, u8 address, u8 value);
      int (* slot_reset) (struct dvb_ca_en50221 *ca, int slot);
      int (* slot_shutdown) (struct dvb_ca_en50221 *ca, int slot);
      int (* slot_ts_enable) (struct dvb_ca_en50221 *ca, int slot);
      int (* poll_slot_status) (struct dvb_ca_en50221 *ca, int slot, int open);
      void * data;
      void * private;
    };


Members
=======

owner
    the module owning this structure

read_attribute_mem
    function for reading attribute memory on the CAM

write_attribute_mem
    function for writing attribute memory on the CAM

read_cam_control
    function for reading the control interface on the CAM

write_cam_control
    function for reading the control interface on the CAM

slot_reset
    function to reset the CAM slot

slot_shutdown
    function to shutdown a CAM slot

slot_ts_enable
    function to enable the Transport Stream on a CAM slot

poll_slot_status
    function to poll slot status. Only necessary if DVB_CA_FLAG_EN50221_IRQ_CAMCHANGE is not set.

data
    private data, used by caller.

private
    Opaque data used by the dvb_ca core. Do not modify!


NOTE
====

the read_⋆, write_⋆ and poll_slot_status functions will be called for different slots concurrently and need to use locks where and if appropriate. There will be no concurrent
access to one slot.
