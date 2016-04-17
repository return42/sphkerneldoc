.. -*- coding: utf-8; mode: rst -*-

====
fw.c
====


.. _`i2400m_bm_cmd_prepare`:

i2400m_bm_cmd_prepare
=====================

.. c:function:: void i2400m_bm_cmd_prepare (struct i2400m_bootrom_header *cmd)

    mode command for delivery

    :param struct i2400m_bootrom_header \*cmd:
        pointer to bootrom header to prepare



.. _`i2400m_bm_cmd_prepare.description`:

Description
-----------

Computes checksum if so needed. After calling this function, DO NOT
modify the command or header as the checksum won't work anymore.

We do it from here because some times we cannot do it in the
original context the command was sent (it is a const), so when we
copy it to our staging buffer, we add the checksum there.



.. _`i2400m_bm_cmd`:

i2400m_bm_cmd
=============

.. c:function:: ssize_t i2400m_bm_cmd (struct i2400m *i2400m, const struct i2400m_bootrom_header *cmd, size_t cmd_size, struct i2400m_bootrom_header *ack, size_t ack_size, int flags)

    Execute a boot mode command

    :param struct i2400m \*i2400m:

        *undescribed*

    :param const struct i2400m_bootrom_header \*cmd:
        buffer containing the command data (pointing at the header).
        This data can be ANYWHERE (for USB, we will copy it to an
        specific buffer). Make sure everything is in proper little
        endian.

    :param size_t cmd_size:
        size of the command. Will be auto padded to the
        bus-specific drivers padding requirements.

    :param struct i2400m_bootrom_header \*ack:
        buffer where to place the acknowledgement. If it is a regular
        command response, all fields will be returned with the right,
        native endianess.

    :param size_t ack_size:
        size of ``ack``\ , 16 aligned; you need to provide at least
        sizeof(\*ack) bytes and then enough to contain the return data
        from the command

    :param int flags:
        see I2400M_BM_CMD\_\* above.



.. _`i2400m_bm_cmd.description`:

Description
-----------

You \*cannot\* use i2400m->bm_ack_buf for this buffer.



.. _`i2400m_bm_cmd.description`:

Description
-----------

You \*cannot\* use i2400m->bm_ack_buf for this buffer.



.. _`i2400m_bm_cmd.denoting-an-error-or`:

denoting an error or
--------------------


-ERESTARTSYS  The device has rebooted

Executes a boot-mode command and waits for a response, doing basic
validation on it; if a zero length response is received, it retries
waiting for a response until a non-zero one is received (timing out
after ``I2400M_BOOT_RETRIES`` retries).



.. _`i2400m_download_chunk`:

i2400m_download_chunk
=====================

.. c:function:: int i2400m_download_chunk (struct i2400m *i2400m, const void *chunk, size_t __chunk_len, unsigned long addr, unsigned int direct, unsigned int do_csum)

    write a single chunk of data to the device's memory

    :param struct i2400m \*i2400m:
        device descriptor

    :param const void \*chunk:

        *undescribed*

    :param size_t __chunk_len:

        *undescribed*

    :param unsigned long addr:
        address in the device memory space

    :param unsigned int direct:
        bootrom write mode

    :param unsigned int do_csum:
        should a checksum validation be performed



.. _`i2400m_bootrom_init`:

i2400m_bootrom_init
===================

.. c:function:: int i2400m_bootrom_init (struct i2400m *i2400m, enum i2400m_bri flags)

    Reboots a powered device into boot mode

    :param struct i2400m \*i2400m:
        device descriptor

    :param enum i2400m_bri flags:

        *undescribed*



.. _`i2400m_bootrom_init.i2400m_bri_soft`:

I2400M_BRI_SOFT
---------------

a reboot barker has been seen
already, so don't wait for it.



.. _`i2400m_bootrom_init.i2400m_bri_no_reboot`:

I2400M_BRI_NO_REBOOT
--------------------

Don't send a reboot command, but wait
for a reboot barker notification. This is a one shot; if
the state machine needs to send a reboot command it will.



.. _`i2400m_bootrom_init.returns`:

Returns
-------


< 0 errno code on error, 0 if ok.



.. _`i2400m_bootrom_init.description`:

Description
-----------


Tries hard enough to put the device in boot-mode. There are two



.. _`i2400m_bootrom_init.main-phases-to-this`:

main phases to this
-------------------


a. (1) send a reboot command and (2) get a reboot barker

b. (1) echo/ack the reboot sending the reboot barker back and (2)
getting an ack barker in return

We want to skip (a) in some cases [soft]. The state machine is
horrible, but it is basically: on each phase, send what has to be
sent (if any), wait for the answer and act on the answer. We might
have to backtrack and retry, so we keep a max tries counter for
that.

It sucks because we don't know ahead of time which is going to be
the reboot barker (the device might send different ones depending
on its EEPROM config) and once the device reboots and waits for the
echo/ack reboot barker being sent back, it doesn't understand
anything else. So we can be left at the point where we don't know
what to send to it -- cold reset and bus reset seem to have little
effect. So the function iterates (in this case) through all the
known barkers and tries them all until an ACK is
received. Otherwise, it gives up.

If we get a timeout after sending a warm reset, we do it again.



.. _`i2400m_dev_bootstrap`:

i2400m_dev_bootstrap
====================

.. c:function:: int i2400m_dev_bootstrap (struct i2400m *i2400m, enum i2400m_bri flags)

    Bring the device to a known state and upload firmware

    :param struct i2400m \*i2400m:
        device descriptor

    :param enum i2400m_bri flags:

        *undescribed*



.. _`i2400m_dev_bootstrap.returns`:

Returns
-------

>= 0 if ok, < 0 errno code on error.

This sets up the firmware upload environment, loads the firmware
file from disk, verifies and then calls the firmware upload process
per se.

Can be called either from probe, or after a warm reset.  Can not be
called from within an interrupt.  All the flow in this code is
single-threade; all I/Os are synchronous.

