.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/mmc/core/core.c

.. _`mmc_request_done`:

mmc_request_done
================

.. c:function:: void mmc_request_done(struct mmc_host *host, struct mmc_request *mrq)

    finish processing an MMC request

    :param struct mmc_host \*host:
        MMC host which completed request

    :param struct mmc_request \*mrq:
        MMC request which request

.. _`mmc_request_done.description`:

Description
-----------

MMC drivers should call this function when they have completed
their processing of a request.

.. _`mmc_start_bkops`:

mmc_start_bkops
===============

.. c:function:: void mmc_start_bkops(struct mmc_card *card, bool from_exception)

    start BKOPS for supported cards

    :param struct mmc_card \*card:
        MMC card to start BKOPS

    :param bool from_exception:
        *undescribed*

.. _`mmc_start_bkops.description`:

Description
-----------

Start background operations whenever requested.
When the urgent BKOPS bit is set in a R1 command response
then background operations should be started immediately.

.. _`mmc_pre_req`:

mmc_pre_req
===========

.. c:function:: void mmc_pre_req(struct mmc_host *host, struct mmc_request *mrq, bool is_first_req)

    Prepare for a new request

    :param struct mmc_host \*host:
        MMC host to prepare command

    :param struct mmc_request \*mrq:
        MMC request to prepare for

    :param bool is_first_req:
        true if there is no previous started request
        that may run in parellel to this call, otherwise false

.. _`mmc_pre_req.description`:

Description
-----------

\ :c:func:`mmc_pre_req`\  is called in prior to \ :c:func:`mmc_start_req`\  to let
host prepare for the new request. Preparation of a request may be
performed while another request is running on the host.

.. _`mmc_post_req`:

mmc_post_req
============

.. c:function:: void mmc_post_req(struct mmc_host *host, struct mmc_request *mrq, int err)

    Post process a completed request

    :param struct mmc_host \*host:
        MMC host to post process command

    :param struct mmc_request \*mrq:
        MMC request to post process for

    :param int err:
        Error, if non zero, clean up any resources made in pre_req

.. _`mmc_post_req.description`:

Description
-----------

Let the host post process a completed request. Post processing of
a request may be performed while another reuqest is running.

.. _`mmc_start_req`:

mmc_start_req
=============

.. c:function:: struct mmc_async_req *mmc_start_req(struct mmc_host *host, struct mmc_async_req *areq, int *error)

    start a non-blocking request

    :param struct mmc_host \*host:
        MMC host to start command

    :param struct mmc_async_req \*areq:
        async request to start

    :param int \*error:
        out parameter returns 0 for success, otherwise non zero

.. _`mmc_start_req.description`:

Description
-----------

Start a new MMC custom command request for a host.
If there is on ongoing async request wait for completion
of that request and start the new one and return.
Does not wait for the new request to complete.

Returns the completed request, NULL in case of none completed.
Wait for the an ongoing request (previoulsy started) to complete and
return the completed request. If there is no ongoing request, NULL
is returned without waiting. NULL is not an error condition.

.. _`mmc_wait_for_req`:

mmc_wait_for_req
================

.. c:function:: void mmc_wait_for_req(struct mmc_host *host, struct mmc_request *mrq)

    start a request and wait for completion

    :param struct mmc_host \*host:
        MMC host to start command

    :param struct mmc_request \*mrq:
        MMC request to start

.. _`mmc_wait_for_req.description`:

Description
-----------

Start a new MMC custom command request for a host, and wait
for the command to complete. Does not attempt to parse the
response.

.. _`mmc_interrupt_hpi`:

mmc_interrupt_hpi
=================

.. c:function:: int mmc_interrupt_hpi(struct mmc_card *card)

    Issue for High priority Interrupt

    :param struct mmc_card \*card:
        the MMC card associated with the HPI transfer

.. _`mmc_interrupt_hpi.description`:

Description
-----------

Issued High Priority Interrupt, and check for card status
until out-of prg-state.

.. _`mmc_wait_for_cmd`:

mmc_wait_for_cmd
================

.. c:function:: int mmc_wait_for_cmd(struct mmc_host *host, struct mmc_command *cmd, int retries)

    start a command and wait for completion

    :param struct mmc_host \*host:
        MMC host to start command

    :param struct mmc_command \*cmd:
        MMC command to start

    :param int retries:
        maximum number of retries

.. _`mmc_wait_for_cmd.description`:

Description
-----------

Start a new MMC command for a host, and wait for the command
to complete.  Return any error that occurred while the command
was executing.  Do not attempt to parse the response.

.. _`mmc_stop_bkops`:

mmc_stop_bkops
==============

.. c:function:: int mmc_stop_bkops(struct mmc_card *card)

    stop ongoing BKOPS

    :param struct mmc_card \*card:
        MMC card to check BKOPS

.. _`mmc_stop_bkops.description`:

Description
-----------

Send HPI command to stop ongoing background operations to
allow rapid servicing of foreground operations, e.g. read/
writes. Wait until the card comes out of the programming state
to avoid errors in servicing read/write requests.

.. _`mmc_set_data_timeout`:

mmc_set_data_timeout
====================

.. c:function:: void mmc_set_data_timeout(struct mmc_data *data, const struct mmc_card *card)

    set the timeout for a data command

    :param struct mmc_data \*data:
        data phase for command

    :param const struct mmc_card \*card:
        the MMC card associated with the data transfer

.. _`mmc_set_data_timeout.description`:

Description
-----------

Computes the data timeout parameters according to the
correct algorithm given the card type.

.. _`mmc_align_data_size`:

mmc_align_data_size
===================

.. c:function:: unsigned int mmc_align_data_size(struct mmc_card *card, unsigned int sz)

    pads a transfer size to a more optimal value

    :param struct mmc_card \*card:
        the MMC card associated with the data transfer

    :param unsigned int sz:
        original transfer size

.. _`mmc_align_data_size.description`:

Description
-----------

Pads the original data size with a number of extra bytes in
order to avoid controller bugs and/or performance hits
(e.g. some controllers revert to PIO for certain sizes).

Returns the improved size, which might be unmodified.

Note that this function is only relevant when issuing a
single scatter gather entry.

.. _`__mmc_claim_host`:

__mmc_claim_host
================

.. c:function:: int __mmc_claim_host(struct mmc_host *host, atomic_t *abort)

    exclusively claim a host

    :param struct mmc_host \*host:
        mmc host to claim

    :param atomic_t \*abort:
        whether or not the operation should be aborted

.. _`__mmc_claim_host.description`:

Description
-----------

Claim a host for a set of operations.  If \ ``abort``\  is non null and
dereference a non-zero value then this will return prematurely with
that non-zero value without acquiring the lock.  Returns zero
with the lock held otherwise.

.. _`mmc_release_host`:

mmc_release_host
================

.. c:function:: void mmc_release_host(struct mmc_host *host)

    release a host

    :param struct mmc_host \*host:
        mmc host to release

.. _`mmc_release_host.description`:

Description
-----------

Release a MMC host, allowing others to claim the host
for their operations.

.. _`mmc_vdd_to_ocrbitnum`:

mmc_vdd_to_ocrbitnum
====================

.. c:function:: int mmc_vdd_to_ocrbitnum(int vdd, bool low_bits)

    Convert a voltage to the OCR bit number

    :param int vdd:
        voltage (mV)

    :param bool low_bits:
        prefer low bits in boundary cases

.. _`mmc_vdd_to_ocrbitnum.description`:

Description
-----------

This function returns the OCR bit number according to the provided \ ``vdd``\ 
value. If conversion is not possible a negative errno value returned.

Depending on the \ ``low_bits``\  flag the function prefers low or high OCR bits
on boundary voltages. For example,
with \ ``low_bits``\  = true, 3300 mV translates to ilog2(MMC_VDD_32_33);
with \ ``low_bits``\  = false, 3300 mV translates to ilog2(MMC_VDD_33_34);

Any value in the [1951:1999] range translates to the ilog2(MMC_VDD_20_21).

.. _`mmc_vddrange_to_ocrmask`:

mmc_vddrange_to_ocrmask
=======================

.. c:function:: u32 mmc_vddrange_to_ocrmask(int vdd_min, int vdd_max)

    Convert a voltage range to the OCR mask

    :param int vdd_min:
        minimum voltage value (mV)

    :param int vdd_max:
        maximum voltage value (mV)

.. _`mmc_vddrange_to_ocrmask.description`:

Description
-----------

This function returns the OCR mask bits according to the provided \ ``vdd_min``\ 
and \ ``vdd_max``\  values. If conversion is not possible the function returns 0.

.. _`mmc_vddrange_to_ocrmask.notes-wrt-boundary-cases`:

Notes wrt boundary cases
------------------------

This function sets the OCR bits for all boundary voltages, for example
[3300:3400] range is translated to MMC_VDD_32_33 \| MMC_VDD_33_34 \|
MMC_VDD_34_35 mask.

.. _`mmc_of_parse_voltage`:

mmc_of_parse_voltage
====================

.. c:function:: int mmc_of_parse_voltage(struct device_node *np, u32 *mask)

    return mask of supported voltages

    :param struct device_node \*np:
        The device node need to be parsed.

    :param u32 \*mask:
        mask of voltages available for MMC/SD/SDIO

.. _`mmc_of_parse_voltage.description`:

Description
-----------

Parse the "voltage-ranges" DT property, returning zero if it is not
found, negative errno if the voltage-range specification is invalid,
or one if the voltage-range is specified and successfully parsed.

.. _`mmc_ocrbitnum_to_vdd`:

mmc_ocrbitnum_to_vdd
====================

.. c:function:: int mmc_ocrbitnum_to_vdd(int vdd_bit, int *min_uV, int *max_uV)

    Convert a OCR bit number to its voltage

    :param int vdd_bit:
        OCR bit number

    :param int \*min_uV:
        minimum voltage value (mV)

    :param int \*max_uV:
        maximum voltage value (mV)

.. _`mmc_ocrbitnum_to_vdd.description`:

Description
-----------

This function returns the voltage range according to the provided OCR
bit number. If conversion is not possible a negative errno value returned.

.. _`mmc_regulator_get_ocrmask`:

mmc_regulator_get_ocrmask
=========================

.. c:function:: int mmc_regulator_get_ocrmask(struct regulator *supply)

    return mask of supported voltages

    :param struct regulator \*supply:
        regulator to use

.. _`mmc_regulator_get_ocrmask.description`:

Description
-----------

This returns either a negative errno, or a mask of voltages that
can be provided to MMC/SD/SDIO devices using the specified voltage
regulator.  This would normally be called before registering the
MMC host adapter.

.. _`mmc_regulator_set_ocr`:

mmc_regulator_set_ocr
=====================

.. c:function:: int mmc_regulator_set_ocr(struct mmc_host *mmc, struct regulator *supply, unsigned short vdd_bit)

    set regulator to match host->ios voltage

    :param struct mmc_host \*mmc:
        the host to regulate

    :param struct regulator \*supply:
        regulator to use

    :param unsigned short vdd_bit:
        zero for power off, else a bit number (host->ios.vdd)

.. _`mmc_regulator_set_ocr.description`:

Description
-----------

Returns zero on success, else negative errno.

MMC host drivers may use this to enable or disable a regulator using
a particular supply voltage.  This would normally be called from the
\ :c:func:`set_ios`\  method.

.. _`mmc_regulator_set_vqmmc`:

mmc_regulator_set_vqmmc
=======================

.. c:function:: int mmc_regulator_set_vqmmc(struct mmc_host *mmc, struct mmc_ios *ios)

    Set VQMMC as per the ios

    :param struct mmc_host \*mmc:
        *undescribed*

    :param struct mmc_ios \*ios:
        *undescribed*

.. _`mmc_regulator_set_vqmmc.description`:

Description
-----------

For 3.3V signaling, we try to match VQMMC to VMMC as closely as possible.
That will match the behavior of old boards where VQMMC and VMMC were supplied
by the same supply.  The Bus Operating conditions for 3.3V signaling in the
SD card spec also define VQMMC in terms of VMMC.
If this is not possible we'll try the full 2.7-3.6V of the spec.

For 1.2V and 1.8V signaling we'll try to get as close as possible to the
requested voltage.  This is definitely a good idea for UHS where there's a
separate regulator on the card that's trying to make 1.8V and it's best if
we match.

This function is expected to be used by a controller's
\ :c:func:`start_signal_voltage_switch`\  function.

.. _`mmc_detect_change`:

mmc_detect_change
=================

.. c:function:: void mmc_detect_change(struct mmc_host *host, unsigned long delay)

    process change of state on a MMC socket

    :param struct mmc_host \*host:
        host which changed state.

    :param unsigned long delay:
        optional delay to wait before detection (jiffies)

.. _`mmc_detect_change.description`:

Description
-----------

MMC drivers should call this when they detect a card has been
inserted or removed. The MMC layer will confirm that any
present card is still functional, and initialize any newly
inserted.

.. _`mmc_erase`:

mmc_erase
=========

.. c:function:: int mmc_erase(struct mmc_card *card, unsigned int from, unsigned int nr, unsigned int arg)

    erase sectors.

    :param struct mmc_card \*card:
        card to erase

    :param unsigned int from:
        first sector to erase

    :param unsigned int nr:
        number of sectors to erase

    :param unsigned int arg:
        erase command argument (SD supports only \ ``MMC_ERASE_ARG``\ )

.. _`mmc_erase.description`:

Description
-----------

Caller must claim host before calling this function.

.. _`mmc_init_context_info`:

mmc_init_context_info
=====================

.. c:function:: void mmc_init_context_info(struct mmc_host *host)

    init synchronization context

    :param struct mmc_host \*host:
        mmc host

.. _`mmc_init_context_info.description`:

Description
-----------

Init struct context_info needed to implement asynchronous
request mechanism, used by mmc core, host driver and mmc requests
supplier.

.. This file was automatic generated / don't edit.
