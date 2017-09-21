.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/ralink/rt2x00/rt2x00usb.h

.. _`rt2x00usb_vendor_request`:

enum rt2x00usb_vendor_request
=============================

.. c:type:: enum rt2x00usb_vendor_request

    USB vendor commands.

.. _`rt2x00usb_vendor_request.definition`:

Definition
----------

.. code-block:: c

    enum rt2x00usb_vendor_request {
        USB_DEVICE_MODE,
        USB_SINGLE_WRITE,
        USB_SINGLE_READ,
        USB_MULTI_WRITE,
        USB_MULTI_READ,
        USB_EEPROM_WRITE,
        USB_EEPROM_READ,
        USB_LED_CONTROL,
        USB_RX_CONTROL
    };

.. _`rt2x00usb_vendor_request.constants`:

Constants
---------

USB_DEVICE_MODE
    *undescribed*

USB_SINGLE_WRITE
    *undescribed*

USB_SINGLE_READ
    *undescribed*

USB_MULTI_WRITE
    *undescribed*

USB_MULTI_READ
    *undescribed*

USB_EEPROM_WRITE
    *undescribed*

USB_EEPROM_READ
    *undescribed*

USB_LED_CONTROL
    *undescribed*

USB_RX_CONTROL
    *undescribed*

.. _`rt2x00usb_mode_offset`:

enum rt2x00usb_mode_offset
==========================

.. c:type:: enum rt2x00usb_mode_offset

    Device modes offset.

.. _`rt2x00usb_mode_offset.definition`:

Definition
----------

.. code-block:: c

    enum rt2x00usb_mode_offset {
        USB_MODE_RESET,
        USB_MODE_UNPLUG,
        USB_MODE_FUNCTION,
        USB_MODE_TEST,
        USB_MODE_SLEEP,
        USB_MODE_FIRMWARE,
        USB_MODE_WAKEUP,
        USB_MODE_AUTORUN
    };

.. _`rt2x00usb_mode_offset.constants`:

Constants
---------

USB_MODE_RESET
    *undescribed*

USB_MODE_UNPLUG
    *undescribed*

USB_MODE_FUNCTION
    *undescribed*

USB_MODE_TEST
    *undescribed*

USB_MODE_SLEEP
    *undescribed*

USB_MODE_FIRMWARE
    *undescribed*

USB_MODE_WAKEUP
    *undescribed*

USB_MODE_AUTORUN
    *undescribed*

.. _`rt2x00usb_vendor_request`:

rt2x00usb_vendor_request
========================

.. c:function:: int rt2x00usb_vendor_request(struct rt2x00_dev *rt2x00dev, const u8 request, const u8 requesttype, const u16 offset, const u16 value, void *buffer, const u16 buffer_length, const int timeout)

    Send register command to device

    :param struct rt2x00_dev \*rt2x00dev:
        Pointer to \ :c:type:`struct rt2x00_dev <rt2x00_dev>`\ 

    :param const u8 request:
        USB vendor command (See \ :c:type:`enum rt2x00usb_vendor_request <rt2x00usb_vendor_request>`\ )

    :param const u8 requesttype:
        Request type \ :c:type:`struct USB_VENDOR_REQUEST <USB_VENDOR_REQUEST>`\ \_\*

    :param const u16 offset:
        Register offset to perform action on

    :param const u16 value:
        Value to write to device

    :param void \*buffer:
        Buffer where information will be read/written to by device

    :param const u16 buffer_length:
        Size of \ :c:type:`struct buffer <buffer>`\ 

    :param const int timeout:
        Operation timeout

.. _`rt2x00usb_vendor_request.description`:

Description
-----------

This is the main function to communicate with the device,
the \ :c:type:`struct buffer <buffer>`\  argument \_must\_ either be NULL or point to
a buffer allocated by kmalloc. Failure to do so can lead
to unexpected behavior depending on the architecture.

.. _`rt2x00usb_vendor_request_buff`:

rt2x00usb_vendor_request_buff
=============================

.. c:function:: int rt2x00usb_vendor_request_buff(struct rt2x00_dev *rt2x00dev, const u8 request, const u8 requesttype, const u16 offset, void *buffer, const u16 buffer_length)

    Send register command to device (buffered)

    :param struct rt2x00_dev \*rt2x00dev:
        Pointer to \ :c:type:`struct rt2x00_dev <rt2x00_dev>`\ 

    :param const u8 request:
        USB vendor command (See \ :c:type:`enum rt2x00usb_vendor_request <rt2x00usb_vendor_request>`\ )

    :param const u8 requesttype:
        Request type \ :c:type:`struct USB_VENDOR_REQUEST <USB_VENDOR_REQUEST>`\ \_\*

    :param const u16 offset:
        Register offset to perform action on

    :param void \*buffer:
        Buffer where information will be read/written to by device

    :param const u16 buffer_length:
        Size of \ :c:type:`struct buffer <buffer>`\ 

.. _`rt2x00usb_vendor_request_buff.description`:

Description
-----------

This function will use a previously with kmalloc allocated cache
to communicate with the device. The contents of the buffer pointer
will be copied to this cache when writing, or read from the cache
when reading.
Buffers send to \ :c:type:`struct rt2x00usb_vendor_request <rt2x00usb_vendor_request>`\  \_must\_ be allocated with
kmalloc. Hence the reason for using a previously allocated cache
which has been allocated properly.

.. _`rt2x00usb_vendor_req_buff_lock`:

rt2x00usb_vendor_req_buff_lock
==============================

.. c:function:: int rt2x00usb_vendor_req_buff_lock(struct rt2x00_dev *rt2x00dev, const u8 request, const u8 requesttype, const u16 offset, void *buffer, const u16 buffer_length, const int timeout)

    Send register command to device (buffered)

    :param struct rt2x00_dev \*rt2x00dev:
        Pointer to \ :c:type:`struct rt2x00_dev <rt2x00_dev>`\ 

    :param const u8 request:
        USB vendor command (See \ :c:type:`enum rt2x00usb_vendor_request <rt2x00usb_vendor_request>`\ )

    :param const u8 requesttype:
        Request type \ :c:type:`struct USB_VENDOR_REQUEST <USB_VENDOR_REQUEST>`\ \_\*

    :param const u16 offset:
        Register offset to perform action on

    :param void \*buffer:
        Buffer where information will be read/written to by device

    :param const u16 buffer_length:
        Size of \ :c:type:`struct buffer <buffer>`\ 

    :param const int timeout:
        Operation timeout

.. _`rt2x00usb_vendor_req_buff_lock.description`:

Description
-----------

A version of \ :c:type:`struct rt2x00usb_vendor_request_buff <rt2x00usb_vendor_request_buff>`\  which must be called
if the usb_cache_mutex is already held.

.. _`rt2x00usb_vendor_request_sw`:

rt2x00usb_vendor_request_sw
===========================

.. c:function:: int rt2x00usb_vendor_request_sw(struct rt2x00_dev *rt2x00dev, const u8 request, const u16 offset, const u16 value, const int timeout)

    Send single register command to device

    :param struct rt2x00_dev \*rt2x00dev:
        Pointer to \ :c:type:`struct rt2x00_dev <rt2x00_dev>`\ 

    :param const u8 request:
        USB vendor command (See \ :c:type:`enum rt2x00usb_vendor_request <rt2x00usb_vendor_request>`\ )

    :param const u16 offset:
        Register offset to perform action on

    :param const u16 value:
        Value to write to device

    :param const int timeout:
        Operation timeout

.. _`rt2x00usb_vendor_request_sw.description`:

Description
-----------

Simple wrapper around rt2x00usb_vendor_request to write a single
command to the device. Since we don't use the buffer argument we
don't have to worry about kmalloc here.

.. _`rt2x00usb_eeprom_read`:

rt2x00usb_eeprom_read
=====================

.. c:function:: int rt2x00usb_eeprom_read(struct rt2x00_dev *rt2x00dev, __le16 *eeprom, const u16 length)

    Read eeprom from device

    :param struct rt2x00_dev \*rt2x00dev:
        Pointer to \ :c:type:`struct rt2x00_dev <rt2x00_dev>`\ 

    :param __le16 \*eeprom:
        Pointer to eeprom array to store the information in

    :param const u16 length:
        Number of bytes to read from the eeprom

.. _`rt2x00usb_eeprom_read.description`:

Description
-----------

Simple wrapper around rt2x00usb_vendor_request to read the eeprom
from the device. Note that the eeprom argument \_must\_ be allocated using
kmalloc for correct handling inside the kernel USB layer.

.. _`rt2x00usb_register_read`:

rt2x00usb_register_read
=======================

.. c:function:: u32 rt2x00usb_register_read(struct rt2x00_dev *rt2x00dev, const unsigned int offset)

    Read 32bit register word

    :param struct rt2x00_dev \*rt2x00dev:
        Device pointer, see \ :c:type:`struct rt2x00_dev <rt2x00_dev>`\ .

    :param const unsigned int offset:
        Register offset

.. _`rt2x00usb_register_read.description`:

Description
-----------

This function is a simple wrapper for 32bit register access
through \ :c:func:`rt2x00usb_vendor_request_buff`\ .

.. _`rt2x00usb_register_read_lock`:

rt2x00usb_register_read_lock
============================

.. c:function:: u32 rt2x00usb_register_read_lock(struct rt2x00_dev *rt2x00dev, const unsigned int offset)

    Read 32bit register word

    :param struct rt2x00_dev \*rt2x00dev:
        Device pointer, see \ :c:type:`struct rt2x00_dev <rt2x00_dev>`\ .

    :param const unsigned int offset:
        Register offset

.. _`rt2x00usb_register_read_lock.description`:

Description
-----------

This function is a simple wrapper for 32bit register access
through \ :c:func:`rt2x00usb_vendor_req_buff_lock`\ .

.. _`rt2x00usb_register_multiread`:

rt2x00usb_register_multiread
============================

.. c:function:: void rt2x00usb_register_multiread(struct rt2x00_dev *rt2x00dev, const unsigned int offset, void *value, const u32 length)

    Read 32bit register words

    :param struct rt2x00_dev \*rt2x00dev:
        Device pointer, see \ :c:type:`struct rt2x00_dev <rt2x00_dev>`\ .

    :param const unsigned int offset:
        Register offset

    :param void \*value:
        Pointer to where register contents should be stored

    :param const u32 length:
        Length of the data

.. _`rt2x00usb_register_multiread.description`:

Description
-----------

This function is a simple wrapper for 32bit register access
through \ :c:func:`rt2x00usb_vendor_request_buff`\ .

.. _`rt2x00usb_register_write`:

rt2x00usb_register_write
========================

.. c:function:: void rt2x00usb_register_write(struct rt2x00_dev *rt2x00dev, const unsigned int offset, u32 value)

    Write 32bit register word

    :param struct rt2x00_dev \*rt2x00dev:
        Device pointer, see \ :c:type:`struct rt2x00_dev <rt2x00_dev>`\ .

    :param const unsigned int offset:
        Register offset

    :param u32 value:
        Data which should be written

.. _`rt2x00usb_register_write.description`:

Description
-----------

This function is a simple wrapper for 32bit register access
through \ :c:func:`rt2x00usb_vendor_request_buff`\ .

.. _`rt2x00usb_register_write_lock`:

rt2x00usb_register_write_lock
=============================

.. c:function:: void rt2x00usb_register_write_lock(struct rt2x00_dev *rt2x00dev, const unsigned int offset, u32 value)

    Write 32bit register word

    :param struct rt2x00_dev \*rt2x00dev:
        Device pointer, see \ :c:type:`struct rt2x00_dev <rt2x00_dev>`\ .

    :param const unsigned int offset:
        Register offset

    :param u32 value:
        Data which should be written

.. _`rt2x00usb_register_write_lock.description`:

Description
-----------

This function is a simple wrapper for 32bit register access
through \ :c:func:`rt2x00usb_vendor_req_buff_lock`\ .

.. _`rt2x00usb_register_multiwrite`:

rt2x00usb_register_multiwrite
=============================

.. c:function:: void rt2x00usb_register_multiwrite(struct rt2x00_dev *rt2x00dev, const unsigned int offset, const void *value, const u32 length)

    Write 32bit register words

    :param struct rt2x00_dev \*rt2x00dev:
        Device pointer, see \ :c:type:`struct rt2x00_dev <rt2x00_dev>`\ .

    :param const unsigned int offset:
        Register offset

    :param const void \*value:
        Data which should be written

    :param const u32 length:
        Length of the data

.. _`rt2x00usb_register_multiwrite.description`:

Description
-----------

This function is a simple wrapper for 32bit register access
through \ :c:func:`rt2x00usb_vendor_request_buff`\ .

.. _`rt2x00usb_regbusy_read`:

rt2x00usb_regbusy_read
======================

.. c:function:: int rt2x00usb_regbusy_read(struct rt2x00_dev *rt2x00dev, const unsigned int offset, const struct rt2x00_field32 field, u32 *reg)

    Read from register with busy check

    :param struct rt2x00_dev \*rt2x00dev:
        Device pointer, see \ :c:type:`struct rt2x00_dev <rt2x00_dev>`\ .

    :param const unsigned int offset:
        Register offset

    :param const struct rt2x00_field32 field:
        Field to check if register is busy

    :param u32 \*reg:
        Pointer to where register contents should be stored

.. _`rt2x00usb_regbusy_read.description`:

Description
-----------

This function will read the given register, and checks if the
register is busy. If it is, it will sleep for a couple of
microseconds before reading the register again. If the register
is not read after a certain timeout, this function will return
FALSE.

.. _`rt2x00usb_register_read_async`:

rt2x00usb_register_read_async
=============================

.. c:function:: void rt2x00usb_register_read_async(struct rt2x00_dev *rt2x00dev, const unsigned int offset, bool (*callback)(struct rt2x00_dev*, int, u32))

    Asynchronously read 32bit register word

    :param struct rt2x00_dev \*rt2x00dev:
        Device pointer, see \ :c:type:`struct rt2x00_dev <rt2x00_dev>`\ .

    :param const unsigned int offset:
        Register offset

    :param bool (\*callback)(struct rt2x00_dev\*, int, u32):
        Functon to call when read completes.

.. _`rt2x00usb_register_read_async.description`:

Description
-----------

Submit a control URB to read a 32bit register. This safe to
be called from atomic context.  The callback will be called
when the URB completes. Otherwise the function is similar
to \ :c:func:`rt2x00usb_register_read`\ .
When the callback function returns false, the memory will be cleaned up,
when it returns true, the urb will be fired again.

.. _`queue_entry_priv_usb`:

struct queue_entry_priv_usb
===========================

.. c:type:: struct queue_entry_priv_usb

    Per entry USB specific information

.. _`queue_entry_priv_usb.definition`:

Definition
----------

.. code-block:: c

    struct queue_entry_priv_usb {
        struct urb *urb;
    }

.. _`queue_entry_priv_usb.members`:

Members
-------

urb
    Urb structure used for device communication.

.. _`queue_entry_priv_usb_bcn`:

struct queue_entry_priv_usb_bcn
===============================

.. c:type:: struct queue_entry_priv_usb_bcn

    Per TX entry USB specific information

.. _`queue_entry_priv_usb_bcn.definition`:

Definition
----------

.. code-block:: c

    struct queue_entry_priv_usb_bcn {
        struct urb *urb;
        unsigned int guardian_data;
        struct urb *guardian_urb;
    }

.. _`queue_entry_priv_usb_bcn.members`:

Members
-------

urb
    Urb structure used for device communication.

guardian_data
    Set to 0, used for sending the guardian data.

guardian_urb
    Urb structure used to send the guardian data.

.. _`queue_entry_priv_usb_bcn.description`:

Description
-----------

The first section should match \ :c:type:`struct queue_entry_priv_usb <queue_entry_priv_usb>`\  exactly.
rt2500usb can use this structure to send a guardian byte when working
with beacons.

.. _`rt2x00usb_kick_queue`:

rt2x00usb_kick_queue
====================

.. c:function:: void rt2x00usb_kick_queue(struct data_queue *queue)

    Kick data queue

    :param struct data_queue \*queue:
        Data queue to kick

.. _`rt2x00usb_kick_queue.description`:

Description
-----------

This will walk through all entries of the queue and push all pending
frames to the hardware as a single burst.

.. _`rt2x00usb_flush_queue`:

rt2x00usb_flush_queue
=====================

.. c:function:: void rt2x00usb_flush_queue(struct data_queue *queue, bool drop)

    Flush data queue

    :param struct data_queue \*queue:
        Data queue to stop

    :param bool drop:
        True to drop all pending frames.

.. _`rt2x00usb_flush_queue.description`:

Description
-----------

This will walk through all entries of the queue and will optionally
kill all URB's which were send to the device, or at least wait until
they have been returned from the device..

.. _`rt2x00usb_watchdog`:

rt2x00usb_watchdog
==================

.. c:function:: void rt2x00usb_watchdog(struct rt2x00_dev *rt2x00dev)

    Watchdog for USB communication

    :param struct rt2x00_dev \*rt2x00dev:
        Pointer to \ :c:type:`struct rt2x00_dev <rt2x00_dev>`\ 

.. _`rt2x00usb_watchdog.description`:

Description
-----------

Check the health of the USB communication and determine
if timeouts have occurred. If this is the case, this function
will reset all communication to restore functionality again.

.. This file was automatic generated / don't edit.

