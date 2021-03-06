.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/tty/synclink_gt.c

.. _`ldisc_receive_buf`:

ldisc_receive_buf
=================

.. c:function:: void ldisc_receive_buf(struct tty_struct *tty, const __u8 *data, char *flags, int count)

    :param tty:
        *undescribed*
    :type tty: struct tty_struct \*

    :param data:
        *undescribed*
    :type data: const __u8 \*

    :param flags:
        *undescribed*
    :type flags: char \*

    :param count:
        *undescribed*
    :type count: int

.. _`ldisc_receive_buf.description`:

Description
-----------

The wrappers maintain line discipline references
while calling into the line discipline.

ldisc_receive_buf  - pass receive data to line discipline

.. _`hdlcdev_attach`:

hdlcdev_attach
==============

.. c:function:: int hdlcdev_attach(struct net_device *dev, unsigned short encoding, unsigned short parity)

    set encoding and frame check sequence (FCS) options

    :param dev:
        *undescribed*
    :type dev: struct net_device \*

    :param encoding:
        *undescribed*
    :type encoding: unsigned short

    :param parity:
        *undescribed*
    :type parity: unsigned short

.. _`hdlcdev_attach.description`:

Description
-----------

dev       pointer to network device structure
encoding  serial encoding setting
parity    FCS setting

returns 0 if success, otherwise error code

.. _`hdlcdev_xmit`:

hdlcdev_xmit
============

.. c:function:: netdev_tx_t hdlcdev_xmit(struct sk_buff *skb, struct net_device *dev)

    :param skb:
        *undescribed*
    :type skb: struct sk_buff \*

    :param dev:
        *undescribed*
    :type dev: struct net_device \*

.. _`hdlcdev_xmit.description`:

Description
-----------

skb  socket buffer containing HDLC frame
dev  pointer to network device structure

.. _`hdlcdev_open`:

hdlcdev_open
============

.. c:function:: int hdlcdev_open(struct net_device *dev)

    claim resources and initialize hardware

    :param dev:
        *undescribed*
    :type dev: struct net_device \*

.. _`hdlcdev_open.description`:

Description
-----------

dev  pointer to network device structure

returns 0 if success, otherwise error code

.. _`hdlcdev_close`:

hdlcdev_close
=============

.. c:function:: int hdlcdev_close(struct net_device *dev)

    shutdown hardware and release resources

    :param dev:
        *undescribed*
    :type dev: struct net_device \*

.. _`hdlcdev_close.description`:

Description
-----------

dev  pointer to network device structure

returns 0 if success, otherwise error code

.. _`hdlcdev_ioctl`:

hdlcdev_ioctl
=============

.. c:function:: int hdlcdev_ioctl(struct net_device *dev, struct ifreq *ifr, int cmd)

    :param dev:
        *undescribed*
    :type dev: struct net_device \*

    :param ifr:
        *undescribed*
    :type ifr: struct ifreq \*

    :param cmd:
        *undescribed*
    :type cmd: int

.. _`hdlcdev_ioctl.description`:

Description
-----------

dev  pointer to network device structure
ifr  pointer to network interface request structure
cmd  IOCTL command code

returns 0 if success, otherwise error code

.. _`hdlcdev_tx_timeout`:

hdlcdev_tx_timeout
==================

.. c:function:: void hdlcdev_tx_timeout(struct net_device *dev)

    :param dev:
        *undescribed*
    :type dev: struct net_device \*

.. _`hdlcdev_tx_timeout.description`:

Description
-----------

dev  pointer to network device structure

.. _`hdlcdev_tx_done`:

hdlcdev_tx_done
===============

.. c:function:: void hdlcdev_tx_done(struct slgt_info *info)

    reenable network layer transmit if stopped

    :param info:
        *undescribed*
    :type info: struct slgt_info \*

.. _`hdlcdev_tx_done.description`:

Description
-----------

info  pointer to device instance information

.. _`hdlcdev_rx`:

hdlcdev_rx
==========

.. c:function:: void hdlcdev_rx(struct slgt_info *info, char *buf, int size)

    pass frame to network layer

    :param info:
        *undescribed*
    :type info: struct slgt_info \*

    :param buf:
        *undescribed*
    :type buf: char \*

    :param size:
        *undescribed*
    :type size: int

.. _`hdlcdev_rx.description`:

Description
-----------

info  pointer to device instance information
buf   pointer to buffer contianing frame data
size  count of data bytes in buf

.. _`hdlcdev_init`:

hdlcdev_init
============

.. c:function:: int hdlcdev_init(struct slgt_info *info)

    do generic HDLC initialization

    :param info:
        *undescribed*
    :type info: struct slgt_info \*

.. _`hdlcdev_init.description`:

Description
-----------

info  pointer to device instance information

returns 0 if success, otherwise error code

.. _`hdlcdev_exit`:

hdlcdev_exit
============

.. c:function:: void hdlcdev_exit(struct slgt_info *info)

    do generic HDLC cleanup

    :param info:
        *undescribed*
    :type info: struct slgt_info \*

.. _`hdlcdev_exit.description`:

Description
-----------

info  pointer to device instance information

.. This file was automatic generated / don't edit.

