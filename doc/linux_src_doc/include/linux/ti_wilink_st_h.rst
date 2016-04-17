.. -*- coding: utf-8; mode: rst -*-

==============
ti_wilink_st.h
==============


.. _`proto_type`:

enum proto_type
===============

.. c:type:: proto_type

    type - The protocol on WiLink chips which share a common physical interface like UART.


.. _`proto_type.definition`:

Definition
----------

.. code-block:: c

    enum proto_type {
      ST_BT,
      ST_FM,
      ST_GPS,
      ST_MAX_CHANNELS
    };


.. _`proto_type.constants`:

Constants
---------

:``ST_BT``:
-- undescribed --

:``ST_FM``:
-- undescribed --

:``ST_GPS``:
-- undescribed --

:``ST_MAX_CHANNELS``:
-- undescribed --


.. _`st_proto_s`:

struct st_proto_s
=================

.. c:type:: st_proto_s

    Per Protocol structure from BT/FM/GPS to ST


.. _`st_proto_s.definition`:

Definition
----------

.. code-block:: c

  struct st_proto_s {
    enum proto_type type;
    long (* recv) (void *, struct sk_buff *);
    unsigned char (* match_packet) (const unsigned char *data);
    void (* reg_complete_cb) (void *, char data);
    long (* write) (struct sk_buff *skb);
    void * priv_data;
    unsigned char chnl_id;
    unsigned short max_frame_size;
    unsigned char hdr_len;
    unsigned char offset_len_in_hdr;
    unsigned char len_size;
    unsigned char reserve;
  };


.. _`st_proto_s.members`:

Members
-------

:``type``:
    type of the protocol being registered among the
    available proto_type(BT, FM, GPS the protocol which share TTY).

:``recv``:
    the receiver callback pointing to a function in the
    protocol drivers called by the ST driver upon receiving
    relevant data.

:``match_packet``:
    reserved for future use, to make ST more generic

:``reg_complete_cb``:
    callback handler pointing to a function in protocol
    handler called by ST when the pending registrations are complete.
    The registrations are marked pending, in situations when fw
    download is in progress.

:``write``:
    pointer to function in ST provided to protocol drivers from ST,
    to be made use when protocol drivers have data to send to TTY.

:``priv_data``:
    privdate data holder for the protocol drivers, sent
    from the protocol drivers during registration, and sent back on
    reg_complete_cb and recv.

:``chnl_id``:
    channel id the protocol driver is interested in, the channel
    id is nothing but the 1st byte of the packet in UART frame.

:``max_frame_size``:
    size of the largest frame the protocol can receive.

:``hdr_len``:
    length of the header structure of the protocol.

:``offset_len_in_hdr``:
    this provides the offset of the length field in the
    header structure of the protocol header, to assist ST to know
    how much to receive, if the data is split across UART frames.

:``len_size``:
    whether the length field inside the header is 2 bytes
    or 1 byte.

:``reserve``:
    the number of bytes ST needs to reserve in the skb being
    prepared for the protocol driver.




.. _`st_data_s`:

struct st_data_s
================

.. c:type:: st_data_s

    ST core internal structure


.. _`st_data_s.definition`:

Definition
----------

.. code-block:: c

  struct st_data_s {
    unsigned long st_state;
    struct sk_buff * tx_skb;
    #define ST_TX_SENDING	1
    #define ST_TX_WAKEUP	2
    unsigned long tx_state;
    struct st_proto_s * list[ST_MAX_CHANNELS];
    unsigned long rx_state;
    unsigned long rx_count;
    struct sk_buff * rx_skb;
    unsigned char rx_chnl;
    struct sk_buff_head txq;
    struct sk_buff_head tx_waitq;
    spinlock_t lock;
    unsigned char protos_registered;
    unsigned long ll_state;
    void * kim_data;
    struct tty_struct * tty;
  };


.. _`st_data_s.members`:

Members
-------

:``st_state``:
    different states of ST like initializing, registration
    in progress, this is mainly used to return relevant err codes
    when protocol drivers are registering. It is also used to track
    the recv function, as in during fw download only HCI events
    can occur , where as during other times other events CH8, CH9
    can occur.

:``tx_skb``:
    If for some reason the tty's write returns lesser bytes written
    then to maintain the rest of data to be written on next instance.
    This needs to be protected, hence the lock inside wakeup func.

:``tx_state``:
    if the data is being written onto the TTY and protocol driver
    wants to send more, queue up data and mark that there is
    more data to send.

:``list[ST_MAX_CHANNELS]``:
    the list of protocols registered, only MAX can exist, one protocol
    can register only once.

:``rx_state``:
    states to be maintained inside st's tty receive

:``rx_count``:
    count to be maintained inside st's tty receieve

:``rx_skb``:
    the skb where all data for a protocol gets accumulated,
    since tty might not call receive when a complete event packet
    is received, the states, count and the skb needs to be maintained.

:``rx_chnl``:
    the channel ID for which the data is getting accumalated for.

:``txq``:
    the list of skbs which needs to be sent onto the TTY.

:``tx_waitq``:
    if the chip is not in AWAKE state, the skbs needs to be queued
    up in here, PM(WAKEUP_IND) data needs to be sent and then the skbs
    from waitq can be moved onto the txq.
    Needs locking too.

:``lock``:
    the lock to protect skbs, queues, and ST states.

:``protos_registered``:
    count of the protocols registered, also when 0 the
    chip enable gpio can be toggled, and when it changes to 1 the fw
    needs to be downloaded to initialize chip side ST.

:``ll_state``:
    the various PM states the chip can be, the states are notified
    to us, when the chip sends relevant PM packets(SLEEP_IND, WAKE_IND).

:``kim_data``:
    reference to the parent encapsulating structure.

:``tty``:
    tty provided by the TTY core for line disciplines.




.. _`st_int_write`:

st_int_write
============

.. c:function:: int st_int_write (const unsigned char *, const unsigned char *,  int)

     point this to tty->driver->write or tty->ops->write depending upon the kernel version

    :param const unsigned char \*:

        *undescribed*

    :param const unsigned char \*:

        *undescribed*

    :param int:

        *undescribed*



.. _`st_write`:

st_write
========

.. c:function:: long st_write (struct sk_buff *)

     internal write function, passed onto protocol drivers via the write function ptr of protocol struct

    :param struct sk_buff \*:

        *undescribed*



.. _`chip_version`:

struct chip_version
===================

.. c:type:: chip_version

    save the chip version


.. _`chip_version.definition`:

Definition
----------

.. code-block:: c

  struct chip_version {
  };


.. _`chip_version.members`:

Members
-------




.. _`kim_data_s`:

struct kim_data_s
=================

.. c:type:: kim_data_s

    the KIM internal data, embedded as the platform's drv data. One for each ST device in the system.


.. _`kim_data_s.definition`:

Definition
----------

.. code-block:: c

  struct kim_data_s {
    long uim_pid;
    struct platform_device * kim_pdev;
    struct completion kim_rcvd;
    struct completion ldisc_installed;
    char resp_buffer[30];
    const struct firmware * fw_entry;
    unsigned long rx_state;
    unsigned long rx_count;
    struct sk_buff * rx_skb;
    struct st_data_s * core_data;
    struct chip_version version;
  };


.. _`kim_data_s.members`:

Members
-------

:``uim_pid``:
    KIM needs to communicate with UIM to request to install
    the ldisc by opening UART when protocol drivers register.

:``kim_pdev``:
    the platform device added in one of the board-XX.c file
    in arch/XX/ directory, 1 for each ST device.

:``kim_rcvd``:
    completion handler to notify when data was received,
    mainly used during fw download, which involves multiple send/wait
    for each of the HCI-VS commands.

:``ldisc_installed``:
    completion handler to notify that the UIM accepted
    the request to install ldisc, notify from tty_open which suggests
    the ldisc was properly installed.

:``resp_buffer[30]``:
    data buffer for the .bts fw file name.

:``fw_entry``:
    firmware class struct to request/release the fw.

:``rx_state``:
    the rx state for kim's receive func during fw download.

:``rx_count``:
    the rx count for the kim's receive func during fw download.

:``rx_skb``:
    all of fw data might not come at once, and hence data storage for
    whole of the fw response, only HCI_EVENTs and hence diff from ST's
    response.

:``core_data``:
    ST core's data, which mainly is the tty's disc_data

:``version``:
    chip version available via a sysfs entry.




.. _`st_kim_start`:

st_kim_start
============

.. c:function:: long st_kim_start (void *)

    :param void \*:

        *undescribed*



.. _`st_kim_start.description`:

Description
-----------

registered, these need to communicate with UIM to request
ldisc installed, read chip_version, download relevant fw



.. _`bts_header`:

struct bts_header
=================

.. c:type:: bts_header

    the fw file is NOT binary which can be sent onto TTY as is. The .bts is more a script file which has different types of actions. Each such action needs to be parsed by the KIM and relevant procedure to be called.


.. _`bts_header.definition`:

Definition
----------

.. code-block:: c

  struct bts_header {
  };


.. _`bts_header.members`:

Members
-------




.. _`bts_action`:

struct bts_action
=================

.. c:type:: bts_action

    Each .bts action has its own type of data.


.. _`bts_action.definition`:

Definition
----------

.. code-block:: c

  struct bts_action {
  };


.. _`bts_action.members`:

Members
-------




.. _`hci_command`:

struct hci_command
==================

.. c:type:: hci_command

    the HCI-VS for intrepreting the change baud rate of host-side UART, which needs to be ignored, since UIM would do that when it receives request from KIM for ldisc installation.


.. _`hci_command.definition`:

Definition
----------

.. code-block:: c

  struct hci_command {
  };


.. _`hci_command.members`:

Members
-------




.. _`st_ll_enable`:

st_ll_enable
============

.. c:function:: void st_ll_enable (struct st_data_s *)

     called by ST Core

    :param struct st_data_s \*:

        *undescribed*



.. _`st_ll_getstate`:

st_ll_getstate
==============

.. c:function:: unsigned long st_ll_getstate (struct st_data_s *)

     of the chip.

    :param struct st_data_s \*:

        *undescribed*



.. _`ti_st_plat_data`:

struct ti_st_plat_data
======================

.. c:type:: ti_st_plat_data

    platform data shared between ST driver and platform specific board file which adds the ST device.


.. _`ti_st_plat_data.definition`:

Definition
----------

.. code-block:: c

  struct ti_st_plat_data {
    u32 nshutdown_gpio;
    unsigned char dev_name[UART_DEV_NAME_LEN];
    u32 flow_cntrl;
    u32 baud_rate;
    int (* resume) (struct platform_device *);
    int (* chip_disable) (struct kim_data_s *);
    int (* chip_awake) (struct kim_data_s *);
  };


.. _`ti_st_plat_data.members`:

Members
-------

:``nshutdown_gpio``:
    Host's GPIO line to which chip's BT_EN is connected.

:``dev_name[UART_DEV_NAME_LEN]``:
    The UART/TTY name to which chip is interfaced. (eg: /dev/ttyS1)

:``flow_cntrl``:
    Should always be 1, since UART's CTS/RTS is used for PM
    purposes.

:``baud_rate``:
    The baud rate supported by the Host UART controller, this will
    be shared across with the chip via a HCI VS command from User-Space Init
    Mgr application.

:``resume``:
    legacy PM routines hooked to platform specific board file, so as
    to take chip-host interface specific action.

:``chip_disable``:
    Platform/Interface specific mux mode setting, GPIO
    configuring, Host side PM disabling etc.. can be done here.

:``chip_awake``:
    Chip specific deep sleep states is communicated to Host
    specific board-xx.c to take actions such as cut UART clocks when chip
    asleep or run host faster when chip awake etc..


