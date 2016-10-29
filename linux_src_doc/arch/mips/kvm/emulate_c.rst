.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/mips/kvm/emulate.c

.. _`kvm_mips_count_disabled`:

kvm_mips_count_disabled
=======================

.. c:function:: int kvm_mips_count_disabled(struct kvm_vcpu *vcpu)

    Find whether the CP0_Count timer is disabled.

    :param struct kvm_vcpu \*vcpu:
        Virtual CPU.

.. _`kvm_mips_count_disabled.return`:

Return
------

1 if the CP0_Count timer is disabled by either the guest
CP0_Cause.DC bit or the count_ctl.DC bit.
0 otherwise (in which case CP0_Count timer is running).

.. _`kvm_mips_ktime_to_count`:

kvm_mips_ktime_to_count
=======================

.. c:function:: uint32_t kvm_mips_ktime_to_count(struct kvm_vcpu *vcpu, ktime_t now)

    Scale ktime_t to a 32-bit count.

    :param struct kvm_vcpu \*vcpu:
        *undescribed*

    :param ktime_t now:
        *undescribed*

.. _`kvm_mips_ktime_to_count.description`:

Description
-----------

Caches the dynamic nanosecond bias in vcpu->arch.count_dyn_bias.

Assumes !kvm_mips_count_disabled(\ ``vcpu``\ ) (guest CP0_Count timer is running).

.. _`kvm_mips_count_time`:

kvm_mips_count_time
===================

.. c:function:: ktime_t kvm_mips_count_time(struct kvm_vcpu *vcpu)

    Get effective current time.

    :param struct kvm_vcpu \*vcpu:
        Virtual CPU.

.. _`kvm_mips_count_time.description`:

Description
-----------

Get effective monotonic ktime. This is usually a straightforward \ :c:func:`ktime_get`\ ,
except when the master disable bit is set in count_ctl, in which case it is
count_resume, i.e. the time that the count was disabled.

.. _`kvm_mips_count_time.return`:

Return
------

Effective monotonic ktime for CP0_Count.

.. _`kvm_mips_read_count_running`:

kvm_mips_read_count_running
===========================

.. c:function:: uint32_t kvm_mips_read_count_running(struct kvm_vcpu *vcpu, ktime_t now)

    Read the current count value as if running.

    :param struct kvm_vcpu \*vcpu:
        Virtual CPU.

    :param ktime_t now:
        Kernel time to read CP0_Count at.

.. _`kvm_mips_read_count_running.description`:

Description
-----------

Returns the current guest CP0_Count register at time \ ``now``\  and handles if the
timer interrupt is pending and hasn't been handled yet.

.. _`kvm_mips_read_count_running.return`:

Return
------

The current value of the guest CP0_Count register.

.. _`kvm_mips_read_count`:

kvm_mips_read_count
===================

.. c:function:: uint32_t kvm_mips_read_count(struct kvm_vcpu *vcpu)

    Read the current count value.

    :param struct kvm_vcpu \*vcpu:
        Virtual CPU.

.. _`kvm_mips_read_count.description`:

Description
-----------

Read the current guest CP0_Count value, taking into account whether the timer
is stopped.

.. _`kvm_mips_read_count.return`:

Return
------

The current guest CP0_Count value.

.. _`kvm_mips_freeze_hrtimer`:

kvm_mips_freeze_hrtimer
=======================

.. c:function:: ktime_t kvm_mips_freeze_hrtimer(struct kvm_vcpu *vcpu, uint32_t *count)

    Safely stop the hrtimer.

    :param struct kvm_vcpu \*vcpu:
        Virtual CPU.

    :param uint32_t \*count:
        Output pointer for CP0_Count value at point of freeze.

.. _`kvm_mips_freeze_hrtimer.description`:

Description
-----------

Freeze the hrtimer safely and return both the ktime and the CP0_Count value
at the point it was frozen. It is guaranteed that any pending interrupts at
the point it was frozen are handled, and none after that point.

This is useful where the time/CP0_Count is needed in the calculation of the
new parameters.

Assumes !kvm_mips_count_disabled(\ ``vcpu``\ ) (guest CP0_Count timer is running).

.. _`kvm_mips_freeze_hrtimer.return`:

Return
------

The ktime at the point of freeze.

.. _`kvm_mips_resume_hrtimer`:

kvm_mips_resume_hrtimer
=======================

.. c:function:: void kvm_mips_resume_hrtimer(struct kvm_vcpu *vcpu, ktime_t now, uint32_t count)

    Resume hrtimer, updating expiry.

    :param struct kvm_vcpu \*vcpu:
        Virtual CPU.

    :param ktime_t now:
        ktime at point of resume.

    :param uint32_t count:
        CP0_Count at point of resume.

.. _`kvm_mips_resume_hrtimer.description`:

Description
-----------

Resumes the timer and updates the timer expiry based on \ ``now``\  and \ ``count``\ .
This can be used in conjunction with \ :c:func:`kvm_mips_freeze_timer`\  when timer
parameters need to be changed.

It is guaranteed that a timer interrupt immediately after resume will be
handled, but not if CP_Compare is exactly at \ ``count``\ . That case is already
handled by \ :c:func:`kvm_mips_freeze_timer`\ .

Assumes !kvm_mips_count_disabled(\ ``vcpu``\ ) (guest CP0_Count timer is running).

.. _`kvm_mips_write_count`:

kvm_mips_write_count
====================

.. c:function:: void kvm_mips_write_count(struct kvm_vcpu *vcpu, uint32_t count)

    Modify the count and update timer.

    :param struct kvm_vcpu \*vcpu:
        Virtual CPU.

    :param uint32_t count:
        Guest CP0_Count value to set.

.. _`kvm_mips_write_count.description`:

Description
-----------

Sets the CP0_Count value and updates the timer accordingly.

.. _`kvm_mips_init_count`:

kvm_mips_init_count
===================

.. c:function:: void kvm_mips_init_count(struct kvm_vcpu *vcpu)

    Initialise timer.

    :param struct kvm_vcpu \*vcpu:
        Virtual CPU.

.. _`kvm_mips_init_count.description`:

Description
-----------

Initialise the timer to a sensible frequency, namely 100MHz, zero it, and set
it going if it's enabled.

.. _`kvm_mips_set_count_hz`:

kvm_mips_set_count_hz
=====================

.. c:function:: int kvm_mips_set_count_hz(struct kvm_vcpu *vcpu, s64 count_hz)

    Update the frequency of the timer.

    :param struct kvm_vcpu \*vcpu:
        Virtual CPU.

    :param s64 count_hz:
        Frequency of CP0_Count timer in Hz.

.. _`kvm_mips_set_count_hz.description`:

Description
-----------

Change the frequency of the CP0_Count timer. This is done atomically so that
CP0_Count is continuous and no timer interrupt is lost.

.. _`kvm_mips_set_count_hz.return`:

Return
------

-EINVAL if \ ``count_hz``\  is out of range.
0 on success.

.. _`kvm_mips_write_compare`:

kvm_mips_write_compare
======================

.. c:function:: void kvm_mips_write_compare(struct kvm_vcpu *vcpu, uint32_t compare, bool ack)

    Modify compare and update timer.

    :param struct kvm_vcpu \*vcpu:
        Virtual CPU.

    :param uint32_t compare:
        New CP0_Compare value.

    :param bool ack:
        Whether to acknowledge timer interrupt.

.. _`kvm_mips_write_compare.description`:

Description
-----------

Update CP0_Compare to a new value and update the timeout.
If \ ``ack``\ , atomically acknowledge any pending timer interrupt, otherwise ensure
any pending timer interrupt is preserved.

.. _`kvm_mips_count_disable`:

kvm_mips_count_disable
======================

.. c:function:: ktime_t kvm_mips_count_disable(struct kvm_vcpu *vcpu)

    Disable count.

    :param struct kvm_vcpu \*vcpu:
        Virtual CPU.

.. _`kvm_mips_count_disable.description`:

Description
-----------

Disable the CP0_Count timer. A timer interrupt on or before the final stop
time will be handled but not after.

Assumes CP0_Count was previously enabled but now Guest.CP0_Cause.DC or
count_ctl.DC has been set (count disabled).

.. _`kvm_mips_count_disable.return`:

Return
------

The time that the timer was stopped.

.. _`kvm_mips_count_disable_cause`:

kvm_mips_count_disable_cause
============================

.. c:function:: void kvm_mips_count_disable_cause(struct kvm_vcpu *vcpu)

    Disable count using CP0_Cause.DC.

    :param struct kvm_vcpu \*vcpu:
        Virtual CPU.

.. _`kvm_mips_count_disable_cause.description`:

Description
-----------

Disable the CP0_Count timer and set CP0_Cause.DC. A timer interrupt on or
before the final stop time will be handled if the timer isn't disabled by
count_ctl.DC, but not after.

Assumes CP0_Cause.DC is clear (count enabled).

.. _`kvm_mips_count_enable_cause`:

kvm_mips_count_enable_cause
===========================

.. c:function:: void kvm_mips_count_enable_cause(struct kvm_vcpu *vcpu)

    Enable count using CP0_Cause.DC.

    :param struct kvm_vcpu \*vcpu:
        Virtual CPU.

.. _`kvm_mips_count_enable_cause.description`:

Description
-----------

Enable the CP0_Count timer and clear CP0_Cause.DC. A timer interrupt after
the start time will be handled if the timer isn't disabled by count_ctl.DC,
potentially before even returning, so the caller should be careful with
ordering of CP0_Cause modifications so as not to lose it.

Assumes CP0_Cause.DC is set (count disabled).

.. _`kvm_mips_set_count_ctl`:

kvm_mips_set_count_ctl
======================

.. c:function:: int kvm_mips_set_count_ctl(struct kvm_vcpu *vcpu, s64 count_ctl)

    Update the count control KVM register.

    :param struct kvm_vcpu \*vcpu:
        Virtual CPU.

    :param s64 count_ctl:
        Count control register new value.

.. _`kvm_mips_set_count_ctl.description`:

Description
-----------

Set the count control KVM register. The timer is updated accordingly.

.. _`kvm_mips_set_count_ctl.return`:

Return
------

-EINVAL if reserved bits are set.
0 on success.

.. _`kvm_mips_set_count_resume`:

kvm_mips_set_count_resume
=========================

.. c:function:: int kvm_mips_set_count_resume(struct kvm_vcpu *vcpu, s64 count_resume)

    Update the count resume KVM register.

    :param struct kvm_vcpu \*vcpu:
        Virtual CPU.

    :param s64 count_resume:
        Count resume register new value.

.. _`kvm_mips_set_count_resume.description`:

Description
-----------

Set the count resume KVM register.

.. _`kvm_mips_set_count_resume.return`:

Return
------

-EINVAL if out of valid range (0..now).
0 on success.

.. _`kvm_mips_count_timeout`:

kvm_mips_count_timeout
======================

.. c:function:: enum hrtimer_restart kvm_mips_count_timeout(struct kvm_vcpu *vcpu)

    Push timer forward on timeout.

    :param struct kvm_vcpu \*vcpu:
        Virtual CPU.

.. _`kvm_mips_count_timeout.description`:

Description
-----------

Handle an hrtimer event by push the hrtimer forward a period.

.. _`kvm_mips_count_timeout.return`:

Return
------

The hrtimer_restart value to return to the hrtimer subsystem.

.. _`kvm_mips_config1_wrmask`:

kvm_mips_config1_wrmask
=======================

.. c:function:: unsigned int kvm_mips_config1_wrmask(struct kvm_vcpu *vcpu)

    Find mask of writable bits in guest Config1

    :param struct kvm_vcpu \*vcpu:
        Virtual CPU.

.. _`kvm_mips_config1_wrmask.description`:

Description
-----------

Finds the mask of bits which are writable in the guest's Config1 CP0
register, by userland (currently read-only to the guest).

.. _`kvm_mips_config3_wrmask`:

kvm_mips_config3_wrmask
=======================

.. c:function:: unsigned int kvm_mips_config3_wrmask(struct kvm_vcpu *vcpu)

    Find mask of writable bits in guest Config3

    :param struct kvm_vcpu \*vcpu:
        Virtual CPU.

.. _`kvm_mips_config3_wrmask.description`:

Description
-----------

Finds the mask of bits which are writable in the guest's Config3 CP0
register, by userland (currently read-only to the guest).

.. _`kvm_mips_config4_wrmask`:

kvm_mips_config4_wrmask
=======================

.. c:function:: unsigned int kvm_mips_config4_wrmask(struct kvm_vcpu *vcpu)

    Find mask of writable bits in guest Config4

    :param struct kvm_vcpu \*vcpu:
        Virtual CPU.

.. _`kvm_mips_config4_wrmask.description`:

Description
-----------

Finds the mask of bits which are writable in the guest's Config4 CP0
register, by userland (currently read-only to the guest).

.. _`kvm_mips_config5_wrmask`:

kvm_mips_config5_wrmask
=======================

.. c:function:: unsigned int kvm_mips_config5_wrmask(struct kvm_vcpu *vcpu)

    Find mask of writable bits in guest Config5

    :param struct kvm_vcpu \*vcpu:
        Virtual CPU.

.. _`kvm_mips_config5_wrmask.description`:

Description
-----------

Finds the mask of bits which are writable in the guest's Config5 CP0
register, by the guest itself.

.. This file was automatic generated / don't edit.
