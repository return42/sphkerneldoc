.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/can/usb/kvaser_usb/kvaser_usb.h

.. _`kvaser_usb_dev_ops`:

struct kvaser_usb_dev_ops
=========================

.. c:type:: struct kvaser_usb_dev_ops

    Device specific functions

.. _`kvaser_usb_dev_ops.definition`:

Definition
----------

.. code-block:: c

    struct kvaser_usb_dev_ops {
        int (*dev_set_mode)(struct net_device *netdev, enum can_mode mode);
        int (*dev_set_bittiming)(struct net_device *netdev);
        int (*dev_set_data_bittiming)(struct net_device *netdev);
        int (*dev_get_berr_counter)(const struct net_device *netdev, struct can_berr_counter *bec);
        int (*dev_setup_endpoints)(struct kvaser_usb *dev);
        int (*dev_init_card)(struct kvaser_usb *dev);
        int (*dev_get_software_info)(struct kvaser_usb *dev);
        int (*dev_get_software_details)(struct kvaser_usb *dev);
        int (*dev_get_card_info)(struct kvaser_usb *dev);
        int (*dev_get_capabilities)(struct kvaser_usb *dev);
        int (*dev_set_opt_mode)(const struct kvaser_usb_net_priv *priv);
        int (*dev_start_chip)(struct kvaser_usb_net_priv *priv);
        int (*dev_stop_chip)(struct kvaser_usb_net_priv *priv);
        int (*dev_reset_chip)(struct kvaser_usb *dev, int channel);
        int (*dev_flush_queue)(struct kvaser_usb_net_priv *priv);
        void (*dev_read_bulk_callback)(struct kvaser_usb *dev, void *buf, int len);
        void *(*dev_frame_to_cmd)(const struct kvaser_usb_net_priv *priv,const struct sk_buff *skb, int *frame_len, int *cmd_len, u16 transid);
    }

.. _`kvaser_usb_dev_ops.members`:

Members
-------

dev_set_mode
    used for can.do_set_mode

dev_set_bittiming
    used for can.do_set_bittiming

dev_set_data_bittiming
    used for can.do_set_data_bittiming

dev_get_berr_counter
    used for can.do_get_berr_counter

dev_setup_endpoints
    setup USB in and out endpoints

dev_init_card
    initialize card

dev_get_software_info
    get software info

dev_get_software_details
    get software details

dev_get_card_info
    get card info

dev_get_capabilities
    discover device capabilities

dev_set_opt_mode
    set ctrlmod

dev_start_chip
    start the CAN controller

dev_stop_chip
    stop the CAN controller

dev_reset_chip
    reset the CAN controller

dev_flush_queue
    flush outstanding CAN messages

dev_read_bulk_callback
    handle incoming commands

dev_frame_to_cmd
    translate struct can_frame into device command

.. This file was automatic generated / don't edit.

