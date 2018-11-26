.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/x86/kernel/apm_32.c

.. _`apm_error`:

apm_error
=========

.. c:function:: void apm_error(char *str, int err)

    display an APM error

    :param str:
        information string
    :type str: char \*

    :param err:
        APM BIOS return code
    :type err: int

.. _`apm_error.description`:

Description
-----------

Write a meaningful log entry to the kernel log in the event of
an APM error.  Note that this also handles (negative) kernel errors.

.. _`__apm_bios_call`:

\__apm_bios_call
================

.. c:function:: long __apm_bios_call(void *_call)

    Make an APM BIOS 32bit call

    :param _call:
        pointer to struct apm_bios_call.
    :type _call: void \*

.. _`__apm_bios_call.description`:

Description
-----------

Make an APM call using the 32bit protected mode interface. The
caller is responsible for knowing if APM BIOS is configured and
enabled. This call can disable interrupts for a long period of
time on some laptops.  The return value is in AH and the carry
flag is loaded into AL.  If there is an error, then the error
code is returned in AH (bits 8-15 of eax) and this function
returns non-zero.

.. _`__apm_bios_call.note`:

Note
----

this makes the call on the current CPU.

.. _`apm_bios_call`:

apm_bios_call
=============

.. c:function:: int apm_bios_call(struct apm_bios_call *call)

    Make an APM BIOS 32bit call (on CPU 0)

    :param call:
        the apm_bios_call registers.
    :type call: struct apm_bios_call \*

.. _`apm_bios_call.description`:

Description
-----------

If there is an error, it is returned in \ ``call.err``\ .

.. _`__apm_bios_call_simple`:

\__apm_bios_call_simple
=======================

.. c:function:: long __apm_bios_call_simple(void *_call)

    Make an APM BIOS 32bit call (on CPU 0)

    :param _call:
        pointer to struct apm_bios_call.
    :type _call: void \*

.. _`__apm_bios_call_simple.description`:

Description
-----------

Make a BIOS call that returns one value only, or just status.
If there is an error, then the error code is returned in AH
(bits 8-15 of eax) and this function returns non-zero (it can
also return -ENOMEM). This is used for simpler BIOS operations.
This call may hold interrupts off for a long time on some laptops.

.. _`__apm_bios_call_simple.note`:

Note
----

this makes the call on the current CPU.

.. _`apm_bios_call_simple`:

apm_bios_call_simple
====================

.. c:function:: int apm_bios_call_simple(u32 func, u32 ebx_in, u32 ecx_in, u32 *eax, int *err)

    make a simple APM BIOS 32bit call

    :param func:
        APM function to invoke
    :type func: u32

    :param ebx_in:
        EBX register value for BIOS call
    :type ebx_in: u32

    :param ecx_in:
        ECX register value for BIOS call
    :type ecx_in: u32

    :param eax:
        EAX register on return from the BIOS call
    :type eax: u32 \*

    :param err:
        bits
    :type err: int \*

.. _`apm_bios_call_simple.description`:

Description
-----------

Make a BIOS call that returns one value only, or just status.
If there is an error, then the error code is returned in \ ``err``\ 
and this function returns non-zero. This is used for simpler
BIOS operations.  This call may hold interrupts off for a long
time on some laptops.

.. _`apm_driver_version`:

apm_driver_version
==================

.. c:function:: int apm_driver_version(u_short *val)

    APM driver version

    :param val:
        loaded with the APM version on return
    :type val: u_short \*

.. _`apm_driver_version.description`:

Description
-----------

Retrieve the APM version supported by the BIOS. This is only
supported for APM 1.1 or higher. An error indicates APM 1.0 is
probably present.

On entry val should point to a value indicating the APM driver
version with the high byte being the major and the low byte the
minor number both in BCD

On return it will hold the BIOS revision supported in the
same format.

.. _`apm_get_event`:

apm_get_event
=============

.. c:function:: int apm_get_event(apm_event_t *event, apm_eventinfo_t *info)

    get an APM event from the BIOS

    :param event:
        pointer to the event
    :type event: apm_event_t \*

    :param info:
        point to the event information
    :type info: apm_eventinfo_t \*

.. _`apm_get_event.description`:

Description
-----------

The APM BIOS provides a polled information for event
reporting. The BIOS expects to be polled at least every second
when events are pending. When a message is found the caller should
poll until no more messages are present.  However, this causes
problems on some laptops where a suspend event notification is
not cleared until it is acknowledged.

Additional information is returned in the info pointer, providing
that APM 1.2 is in use. If no messges are pending the value 0x80
is returned (No power management events pending).

.. _`set_power_state`:

set_power_state
===============

.. c:function:: int set_power_state(u_short what, u_short state)

    set the power management state

    :param what:
        which items to transition
    :type what: u_short

    :param state:
        state to transition to
    :type state: u_short

.. _`set_power_state.description`:

Description
-----------

Request an APM change of state for one or more system devices. The
processor state must be transitioned last of all. what holds the
class of device in the upper byte and the device number (0xFF for
all) for the object to be transitioned.

The state holds the state to transition to, which may in fact
be an acceptance of a BIOS requested state change.

.. _`set_system_power_state`:

set_system_power_state
======================

.. c:function:: int set_system_power_state(u_short state)

    set system wide power state

    :param state:
        which state to enter
    :type state: u_short

.. _`set_system_power_state.description`:

Description
-----------

Transition the entire system into a new APM power state.

.. _`apm_do_idle`:

apm_do_idle
===========

.. c:function:: int apm_do_idle( void)

    perform power saving

    :param void:
        no arguments
    :type void: 

.. _`apm_do_idle.description`:

Description
-----------

This function notifies the BIOS that the processor is (in the view
of the OS) idle. It returns -1 in the event that the BIOS refuses
to handle the idle request. On a success the function returns 1
if the BIOS did clock slowing or 0 otherwise.

.. _`apm_do_busy`:

apm_do_busy
===========

.. c:function:: void apm_do_busy( void)

    inform the BIOS the CPU is busy

    :param void:
        no arguments
    :type void: 

.. _`apm_do_busy.description`:

Description
-----------

Request that the BIOS brings the CPU back to full performance.

.. _`apm_cpu_idle`:

apm_cpu_idle
============

.. c:function:: int apm_cpu_idle(struct cpuidle_device *dev, struct cpuidle_driver *drv, int index)

    cpu idling for APM capable Linux

    :param dev:
        *undescribed*
    :type dev: struct cpuidle_device \*

    :param drv:
        *undescribed*
    :type drv: struct cpuidle_driver \*

    :param index:
        *undescribed*
    :type index: int

.. _`apm_cpu_idle.description`:

Description
-----------

This is the idling function the kernel executes when APM is available. It
tries to do BIOS powermanagement based on the average system idle time.
Furthermore it calls the system default idle routine.

.. _`apm_power_off`:

apm_power_off
=============

.. c:function:: void apm_power_off( void)

    ask the BIOS to power off

    :param void:
        no arguments
    :type void: 

.. _`apm_power_off.description`:

Description
-----------

Handle the power off sequence. This is the one piece of code we
will execute even on SMP machines. In order to deal with BIOS
bugs we support real mode APM BIOS power off calls. We also make
the SMP call on CPU0 as some systems will only honour this call
on their first cpu.

.. _`apm_enable_power_management`:

apm_enable_power_management
===========================

.. c:function:: int apm_enable_power_management(int enable)

    enable BIOS APM power management

    :param enable:
        enable yes/no
    :type enable: int

.. _`apm_enable_power_management.description`:

Description
-----------

Enable or disable the APM BIOS power services.

.. _`apm_get_power_status`:

apm_get_power_status
====================

.. c:function:: int apm_get_power_status(u_short *status, u_short *bat, u_short *life)

    get current power state

    :param status:
        returned status
    :type status: u_short \*

    :param bat:
        battery info
    :type bat: u_short \*

    :param life:
        estimated life
    :type life: u_short \*

.. _`apm_get_power_status.description`:

Description
-----------

Obtain the current power status from the APM BIOS. We return a
status which gives the rough battery status, and current power
source. The bat value returned give an estimate as a percentage
of life and a status value for the battery. The estimated life
if reported is a lifetime in secodnds/minutes at current powwer
consumption.

.. _`apm_engage_power_management`:

apm_engage_power_management
===========================

.. c:function:: int apm_engage_power_management(u_short device, int enable)

    enable PM on a device

    :param device:
        identity of device
    :type device: u_short

    :param enable:
        on/off
    :type enable: int

.. _`apm_engage_power_management.description`:

Description
-----------

Activate or deactivate power management on either a specific device
or the entire system (%APM_DEVICE_ALL).

.. _`apm_console_blank`:

apm_console_blank
=================

.. c:function:: int apm_console_blank(int blank)

    blank the display

    :param blank:
        on/off
    :type blank: int

.. _`apm_console_blank.description`:

Description
-----------

Attempt to blank the console, firstly by blanking just video device
zero, and if that fails (some BIOSes don't support it) then it blanks
all video devices. Typically the BIOS will do laptop backlight and
monitor powerdown for us.

.. This file was automatic generated / don't edit.

