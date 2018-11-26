.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/s390/cio/device_ops.c

.. _`ccw_device_set_options_mask`:

ccw_device_set_options_mask
===========================

.. c:function:: int ccw_device_set_options_mask(struct ccw_device *cdev, unsigned long flags)

    set some options and unset the rest

    :param cdev:
        device for which the options are to be set
    :type cdev: struct ccw_device \*

    :param flags:
        options to be set
    :type flags: unsigned long

.. _`ccw_device_set_options_mask.description`:

Description
-----------

All flags specified in \ ``flags``\  are set, all flags not specified in \ ``flags``\ 
are cleared.

.. _`ccw_device_set_options_mask.return`:

Return
------

  \ ``0``\  on success, -%EINVAL on an invalid flag combination.

.. _`ccw_device_set_options`:

ccw_device_set_options
======================

.. c:function:: int ccw_device_set_options(struct ccw_device *cdev, unsigned long flags)

    set some options

    :param cdev:
        device for which the options are to be set
    :type cdev: struct ccw_device \*

    :param flags:
        options to be set
    :type flags: unsigned long

.. _`ccw_device_set_options.description`:

Description
-----------

All flags specified in \ ``flags``\  are set, the remainder is left untouched.

.. _`ccw_device_set_options.return`:

Return
------

  \ ``0``\  on success, -%EINVAL if an invalid flag combination would ensue.

.. _`ccw_device_clear_options`:

ccw_device_clear_options
========================

.. c:function:: void ccw_device_clear_options(struct ccw_device *cdev, unsigned long flags)

    clear some options

    :param cdev:
        device for which the options are to be cleared
    :type cdev: struct ccw_device \*

    :param flags:
        options to be cleared
    :type flags: unsigned long

.. _`ccw_device_clear_options.description`:

Description
-----------

All flags specified in \ ``flags``\  are cleared, the remainder is left untouched.

.. _`ccw_device_is_pathgroup`:

ccw_device_is_pathgroup
=======================

.. c:function:: int ccw_device_is_pathgroup(struct ccw_device *cdev)

    determine if paths to this device are grouped

    :param cdev:
        ccw device
    :type cdev: struct ccw_device \*

.. _`ccw_device_is_pathgroup.description`:

Description
-----------

Return non-zero if there is a path group, zero otherwise.

.. _`ccw_device_is_multipath`:

ccw_device_is_multipath
=======================

.. c:function:: int ccw_device_is_multipath(struct ccw_device *cdev)

    determine if device is operating in multipath mode

    :param cdev:
        ccw device
    :type cdev: struct ccw_device \*

.. _`ccw_device_is_multipath.description`:

Description
-----------

Return non-zero if device is operating in multipath mode, zero otherwise.

.. _`ccw_device_clear`:

ccw_device_clear
================

.. c:function:: int ccw_device_clear(struct ccw_device *cdev, unsigned long intparm)

    terminate I/O request processing

    :param cdev:
        target ccw device
    :type cdev: struct ccw_device \*

    :param intparm:
        interruption parameter; value is only used if no I/O is
        outstanding, otherwise the intparm associated with the I/O request
        is returned
    :type intparm: unsigned long

.. _`ccw_device_clear.description`:

Description
-----------

\ :c:func:`ccw_device_clear`\  calls csch on \ ``cdev``\ 's subchannel.

.. _`ccw_device_clear.return`:

Return
------

 \ ``0``\  on success,
 -%ENODEV on device not operational,
 -%EINVAL on invalid device state.

.. _`ccw_device_clear.context`:

Context
-------

 Interrupts disabled, ccw device lock held

.. _`ccw_device_start_timeout_key`:

ccw_device_start_timeout_key
============================

.. c:function:: int ccw_device_start_timeout_key(struct ccw_device *cdev, struct ccw1 *cpa, unsigned long intparm, __u8 lpm, __u8 key, unsigned long flags, int expires)

    start a s390 channel program with timeout and key

    :param cdev:
        target ccw device
    :type cdev: struct ccw_device \*

    :param cpa:
        logical start address of channel program
    :type cpa: struct ccw1 \*

    :param intparm:
        user specific interruption parameter; will be presented back to
        \ ``cdev``\ 's interrupt handler. Allows a device driver to associate
        the interrupt with a particular I/O request.
    :type intparm: unsigned long

    :param lpm:
        defines the channel path to be used for a specific I/O request. A
        value of 0 will make cio use the opm.
    :type lpm: __u8

    :param key:
        storage key to be used for the I/O
    :type key: __u8

    :param flags:
        additional flags; defines the action to be performed for I/O
        processing.
    :type flags: unsigned long

    :param expires:
        timeout value in jiffies
    :type expires: int

.. _`ccw_device_start_timeout_key.description`:

Description
-----------

Start a S/390 channel program. When the interrupt arrives, the
IRQ handler is called, either immediately, delayed (dev-end missing,
or sense required) or never (no IRQ handler registered).
This function notifies the device driver if the channel program has not
completed during the time specified by \ ``expires``\ . If a timeout occurs, the
channel program is terminated via xsch, hsch or csch, and the device's
interrupt handler will be called with an irb containing ERR_PTR(-%ETIMEDOUT).

.. _`ccw_device_start_timeout_key.return`:

Return
------

 \ ``0``\ , if the operation was successful;
 -%EBUSY, if the device is busy, or status pending;
 -%EACCES, if no path specified in \ ``lpm``\  is operational;
 -%ENODEV, if the device is not operational.

.. _`ccw_device_start_timeout_key.context`:

Context
-------

 Interrupts disabled, ccw device lock held

.. _`ccw_device_start_key`:

ccw_device_start_key
====================

.. c:function:: int ccw_device_start_key(struct ccw_device *cdev, struct ccw1 *cpa, unsigned long intparm, __u8 lpm, __u8 key, unsigned long flags)

    start a s390 channel program with key

    :param cdev:
        target ccw device
    :type cdev: struct ccw_device \*

    :param cpa:
        logical start address of channel program
    :type cpa: struct ccw1 \*

    :param intparm:
        user specific interruption parameter; will be presented back to
        \ ``cdev``\ 's interrupt handler. Allows a device driver to associate
        the interrupt with a particular I/O request.
    :type intparm: unsigned long

    :param lpm:
        defines the channel path to be used for a specific I/O request. A
        value of 0 will make cio use the opm.
    :type lpm: __u8

    :param key:
        storage key to be used for the I/O
    :type key: __u8

    :param flags:
        additional flags; defines the action to be performed for I/O
        processing.
    :type flags: unsigned long

.. _`ccw_device_start_key.description`:

Description
-----------

Start a S/390 channel program. When the interrupt arrives, the
IRQ handler is called, either immediately, delayed (dev-end missing,
or sense required) or never (no IRQ handler registered).

.. _`ccw_device_start_key.return`:

Return
------

 \ ``0``\ , if the operation was successful;
 -%EBUSY, if the device is busy, or status pending;
 -%EACCES, if no path specified in \ ``lpm``\  is operational;
 -%ENODEV, if the device is not operational.

.. _`ccw_device_start_key.context`:

Context
-------

 Interrupts disabled, ccw device lock held

.. _`ccw_device_start`:

ccw_device_start
================

.. c:function:: int ccw_device_start(struct ccw_device *cdev, struct ccw1 *cpa, unsigned long intparm, __u8 lpm, unsigned long flags)

    start a s390 channel program

    :param cdev:
        target ccw device
    :type cdev: struct ccw_device \*

    :param cpa:
        logical start address of channel program
    :type cpa: struct ccw1 \*

    :param intparm:
        user specific interruption parameter; will be presented back to
        \ ``cdev``\ 's interrupt handler. Allows a device driver to associate
        the interrupt with a particular I/O request.
    :type intparm: unsigned long

    :param lpm:
        defines the channel path to be used for a specific I/O request. A
        value of 0 will make cio use the opm.
    :type lpm: __u8

    :param flags:
        additional flags; defines the action to be performed for I/O
        processing.
    :type flags: unsigned long

.. _`ccw_device_start.description`:

Description
-----------

Start a S/390 channel program. When the interrupt arrives, the
IRQ handler is called, either immediately, delayed (dev-end missing,
or sense required) or never (no IRQ handler registered).

.. _`ccw_device_start.return`:

Return
------

 \ ``0``\ , if the operation was successful;
 -%EBUSY, if the device is busy, or status pending;
 -%EACCES, if no path specified in \ ``lpm``\  is operational;
 -%ENODEV, if the device is not operational.

.. _`ccw_device_start.context`:

Context
-------

 Interrupts disabled, ccw device lock held

.. _`ccw_device_start_timeout`:

ccw_device_start_timeout
========================

.. c:function:: int ccw_device_start_timeout(struct ccw_device *cdev, struct ccw1 *cpa, unsigned long intparm, __u8 lpm, unsigned long flags, int expires)

    start a s390 channel program with timeout

    :param cdev:
        target ccw device
    :type cdev: struct ccw_device \*

    :param cpa:
        logical start address of channel program
    :type cpa: struct ccw1 \*

    :param intparm:
        user specific interruption parameter; will be presented back to
        \ ``cdev``\ 's interrupt handler. Allows a device driver to associate
        the interrupt with a particular I/O request.
    :type intparm: unsigned long

    :param lpm:
        defines the channel path to be used for a specific I/O request. A
        value of 0 will make cio use the opm.
    :type lpm: __u8

    :param flags:
        additional flags; defines the action to be performed for I/O
        processing.
    :type flags: unsigned long

    :param expires:
        timeout value in jiffies
    :type expires: int

.. _`ccw_device_start_timeout.description`:

Description
-----------

Start a S/390 channel program. When the interrupt arrives, the
IRQ handler is called, either immediately, delayed (dev-end missing,
or sense required) or never (no IRQ handler registered).
This function notifies the device driver if the channel program has not
completed during the time specified by \ ``expires``\ . If a timeout occurs, the
channel program is terminated via xsch, hsch or csch, and the device's
interrupt handler will be called with an irb containing ERR_PTR(-%ETIMEDOUT).

.. _`ccw_device_start_timeout.return`:

Return
------

 \ ``0``\ , if the operation was successful;
 -%EBUSY, if the device is busy, or status pending;
 -%EACCES, if no path specified in \ ``lpm``\  is operational;
 -%ENODEV, if the device is not operational.

.. _`ccw_device_start_timeout.context`:

Context
-------

 Interrupts disabled, ccw device lock held

.. _`ccw_device_halt`:

ccw_device_halt
===============

.. c:function:: int ccw_device_halt(struct ccw_device *cdev, unsigned long intparm)

    halt I/O request processing

    :param cdev:
        target ccw device
    :type cdev: struct ccw_device \*

    :param intparm:
        interruption parameter; value is only used if no I/O is
        outstanding, otherwise the intparm associated with the I/O request
        is returned
    :type intparm: unsigned long

.. _`ccw_device_halt.description`:

Description
-----------

\ :c:func:`ccw_device_halt`\  calls hsch on \ ``cdev``\ 's subchannel.

.. _`ccw_device_halt.return`:

Return
------

 \ ``0``\  on success,
 -%ENODEV on device not operational,
 -%EINVAL on invalid device state,
 -%EBUSY on device busy or interrupt pending.

.. _`ccw_device_halt.context`:

Context
-------

 Interrupts disabled, ccw device lock held

.. _`ccw_device_resume`:

ccw_device_resume
=================

.. c:function:: int ccw_device_resume(struct ccw_device *cdev)

    resume channel program execution

    :param cdev:
        target ccw device
    :type cdev: struct ccw_device \*

.. _`ccw_device_resume.description`:

Description
-----------

\ :c:func:`ccw_device_resume`\  calls rsch on \ ``cdev``\ 's subchannel.

.. _`ccw_device_resume.return`:

Return
------

 \ ``0``\  on success,
 -%ENODEV on device not operational,
 -%EINVAL on invalid device state,
 -%EBUSY on device busy or interrupt pending.

.. _`ccw_device_resume.context`:

Context
-------

 Interrupts disabled, ccw device lock held

.. _`ccw_device_get_ciw`:

ccw_device_get_ciw
==================

.. c:function:: struct ciw *ccw_device_get_ciw(struct ccw_device *cdev, __u32 ct)

    Search for CIW command in extended sense data.

    :param cdev:
        ccw device to inspect
    :type cdev: struct ccw_device \*

    :param ct:
        command type to look for
    :type ct: __u32

.. _`ccw_device_get_ciw.description`:

Description
-----------

During SenseID, command information words (CIWs) describing special
commands available to the device may have been stored in the extended
sense data. This function searches for CIWs of a specified command
type in the extended sense data.

.. _`ccw_device_get_ciw.return`:

Return
------

 \ ``NULL``\  if no extended sense data has been stored or if no CIW of the
 specified command type could be found,
 else a pointer to the CIW of the specified command type.

.. _`ccw_device_get_path_mask`:

ccw_device_get_path_mask
========================

.. c:function:: __u8 ccw_device_get_path_mask(struct ccw_device *cdev)

    get currently available paths

    :param cdev:
        ccw device to be queried
    :type cdev: struct ccw_device \*

.. _`ccw_device_get_path_mask.return`:

Return
------

 \ ``0``\  if no subchannel for the device is available,
 else the mask of currently available paths for the ccw device's subchannel.

.. _`ccw_device_get_chp_desc`:

ccw_device_get_chp_desc
=======================

.. c:function:: struct channel_path_desc_fmt0 *ccw_device_get_chp_desc(struct ccw_device *cdev, int chp_idx)

    return newly allocated channel-path descriptor

    :param cdev:
        device to obtain the descriptor for
    :type cdev: struct ccw_device \*

    :param chp_idx:
        index of the channel path
    :type chp_idx: int

.. _`ccw_device_get_chp_desc.description`:

Description
-----------

On success return a newly allocated copy of the channel-path description
data associated with the given channel path. Return \ ``NULL``\  on error.

.. _`ccw_device_get_util_str`:

ccw_device_get_util_str
=======================

.. c:function:: u8 *ccw_device_get_util_str(struct ccw_device *cdev, int chp_idx)

    return newly allocated utility strings

    :param cdev:
        device to obtain the utility strings for
    :type cdev: struct ccw_device \*

    :param chp_idx:
        index of the channel path
    :type chp_idx: int

.. _`ccw_device_get_util_str.description`:

Description
-----------

On success return a newly allocated copy of the utility strings
associated with the given channel path. Return \ ``NULL``\  on error.

.. _`ccw_device_get_id`:

ccw_device_get_id
=================

.. c:function:: void ccw_device_get_id(struct ccw_device *cdev, struct ccw_dev_id *dev_id)

    obtain a ccw device id

    :param cdev:
        device to obtain the id for
    :type cdev: struct ccw_device \*

    :param dev_id:
        where to fill in the values
    :type dev_id: struct ccw_dev_id \*

.. _`ccw_device_tm_start_timeout_key`:

ccw_device_tm_start_timeout_key
===============================

.. c:function:: int ccw_device_tm_start_timeout_key(struct ccw_device *cdev, struct tcw *tcw, unsigned long intparm, u8 lpm, u8 key, int expires)

    perform start function

    :param cdev:
        ccw device on which to perform the start function
    :type cdev: struct ccw_device \*

    :param tcw:
        transport-command word to be started
    :type tcw: struct tcw \*

    :param intparm:
        user defined parameter to be passed to the interrupt handler
    :type intparm: unsigned long

    :param lpm:
        mask of paths to use
    :type lpm: u8

    :param key:
        storage key to use for storage access
    :type key: u8

    :param expires:
        time span in jiffies after which to abort request
    :type expires: int

.. _`ccw_device_tm_start_timeout_key.description`:

Description
-----------

Start the tcw on the given ccw device. Return zero on success, non-zero
otherwise.

.. _`ccw_device_tm_start_key`:

ccw_device_tm_start_key
=======================

.. c:function:: int ccw_device_tm_start_key(struct ccw_device *cdev, struct tcw *tcw, unsigned long intparm, u8 lpm, u8 key)

    perform start function

    :param cdev:
        ccw device on which to perform the start function
    :type cdev: struct ccw_device \*

    :param tcw:
        transport-command word to be started
    :type tcw: struct tcw \*

    :param intparm:
        user defined parameter to be passed to the interrupt handler
    :type intparm: unsigned long

    :param lpm:
        mask of paths to use
    :type lpm: u8

    :param key:
        storage key to use for storage access
    :type key: u8

.. _`ccw_device_tm_start_key.description`:

Description
-----------

Start the tcw on the given ccw device. Return zero on success, non-zero
otherwise.

.. _`ccw_device_tm_start`:

ccw_device_tm_start
===================

.. c:function:: int ccw_device_tm_start(struct ccw_device *cdev, struct tcw *tcw, unsigned long intparm, u8 lpm)

    perform start function

    :param cdev:
        ccw device on which to perform the start function
    :type cdev: struct ccw_device \*

    :param tcw:
        transport-command word to be started
    :type tcw: struct tcw \*

    :param intparm:
        user defined parameter to be passed to the interrupt handler
    :type intparm: unsigned long

    :param lpm:
        mask of paths to use
    :type lpm: u8

.. _`ccw_device_tm_start.description`:

Description
-----------

Start the tcw on the given ccw device. Return zero on success, non-zero
otherwise.

.. _`ccw_device_tm_start_timeout`:

ccw_device_tm_start_timeout
===========================

.. c:function:: int ccw_device_tm_start_timeout(struct ccw_device *cdev, struct tcw *tcw, unsigned long intparm, u8 lpm, int expires)

    perform start function

    :param cdev:
        ccw device on which to perform the start function
    :type cdev: struct ccw_device \*

    :param tcw:
        transport-command word to be started
    :type tcw: struct tcw \*

    :param intparm:
        user defined parameter to be passed to the interrupt handler
    :type intparm: unsigned long

    :param lpm:
        mask of paths to use
    :type lpm: u8

    :param expires:
        time span in jiffies after which to abort request
    :type expires: int

.. _`ccw_device_tm_start_timeout.description`:

Description
-----------

Start the tcw on the given ccw device. Return zero on success, non-zero
otherwise.

.. _`ccw_device_get_mdc`:

ccw_device_get_mdc
==================

.. c:function:: int ccw_device_get_mdc(struct ccw_device *cdev, u8 mask)

    accumulate max data count

    :param cdev:
        ccw device for which the max data count is accumulated
    :type cdev: struct ccw_device \*

    :param mask:
        mask of paths to use
    :type mask: u8

.. _`ccw_device_get_mdc.description`:

Description
-----------

Return the number of 64K-bytes blocks all paths at least support
for a transport command. Return values <= 0 indicate failures.

.. _`ccw_device_tm_intrg`:

ccw_device_tm_intrg
===================

.. c:function:: int ccw_device_tm_intrg(struct ccw_device *cdev)

    perform interrogate function

    :param cdev:
        ccw device on which to perform the interrogate function
    :type cdev: struct ccw_device \*

.. _`ccw_device_tm_intrg.description`:

Description
-----------

Perform an interrogate function on the given ccw device. Return zero on
success, non-zero otherwise.

.. _`ccw_device_get_schid`:

ccw_device_get_schid
====================

.. c:function:: void ccw_device_get_schid(struct ccw_device *cdev, struct subchannel_id *schid)

    obtain a subchannel id

    :param cdev:
        device to obtain the id for
    :type cdev: struct ccw_device \*

    :param schid:
        where to fill in the values
    :type schid: struct subchannel_id \*

.. This file was automatic generated / don't edit.

