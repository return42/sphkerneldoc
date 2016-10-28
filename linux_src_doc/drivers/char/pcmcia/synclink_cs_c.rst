.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/char/pcmcia/synclink_cs.c

.. _`ldisc_receive_buf`:

ldisc_receive_buf
=================

.. c:function:: void ldisc_receive_buf(struct tty_struct *tty, const __u8 *data, char *flags, int count)

    :param struct tty_struct \*tty:
        *undescribed*

    :param const __u8 \*data:
        *undescribed*

    :param char \*flags:
        *undescribed*

    :param int count:
        *undescribed*

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

    :param struct net_device \*dev:
        *undescribed*

    :param unsigned short encoding:
        *undescribed*

    :param unsigned short parity:
        *undescribed*

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

    :param struct sk_buff \*skb:
        *undescribed*

    :param struct net_device \*dev:
        *undescribed*

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

    :param struct net_device \*dev:
        *undescribed*

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

    :param struct net_device \*dev:
        *undescribed*

.. _`hdlcdev_close.description`:

Description
-----------

dev  pointer to network device structure

returns 0 if success, otherwise error code

.. _`hdlcdev_ioctl`:

hdlcdev_ioctl
=============

.. c:function:: int hdlcdev_ioctl(struct net_device *dev, struct ifreq *ifr, int cmd)

    :param struct net_device \*dev:
        *undescribed*

    :param struct ifreq \*ifr:
        *undescribed*

    :param int cmd:
        *undescribed*

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

    :param struct net_device \*dev:
        *undescribed*

.. _`hdlcdev_tx_timeout.description`:

Description
-----------

dev  pointer to network device structure

.. _`hdlcdev_tx_done`:

hdlcdev_tx_done
===============

.. c:function:: void hdlcdev_tx_done(MGSLPC_INFO *info)

    reenable network layer transmit if stopped

    :param MGSLPC_INFO \*info:
        *undescribed*

.. _`hdlcdev_tx_done.description`:

Description
-----------

info  pointer to device instance information

.. _`hdlcdev_rx`:

hdlcdev_rx
==========

.. c:function:: void hdlcdev_rx(MGSLPC_INFO *info, char *buf, int size)

    pass frame to network layer

    :param MGSLPC_INFO \*info:
        *undescribed*

    :param char \*buf:
        *undescribed*

    :param int size:
        *undescribed*

.. _`hdlcdev_rx.description`:

Description
-----------

info  pointer to device instance information
buf   pointer to buffer contianing frame data
size  count of data bytes in buf

.. _`hdlcdev_init`:

hdlcdev_init
============

.. c:function:: int hdlcdev_init(MGSLPC_INFO *info)

    do generic HDLC initialization

    :param MGSLPC_INFO \*info:
        *undescribed*

.. _`hdlcdev_init.description`:

Description
-----------

info  pointer to device instance information

returns 0 if success, otherwise error code

.. _`hdlcdev_exit`:

hdlcdev_exit
============

.. c:function:: void hdlcdev_exit(MGSLPC_INFO *info)

    do generic HDLC cleanup

    :param MGSLPC_INFO \*info:
        *undescribed*

.. _`hdlcdev_exit.description`:

Description
-----------

info  pointer to device instance information

.. This file was automatic generated / don't edit.

