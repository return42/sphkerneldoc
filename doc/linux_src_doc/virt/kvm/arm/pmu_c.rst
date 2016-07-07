.. -*- coding: utf-8; mode: rst -*-
.. src-file: virt/kvm/arm/pmu.c

.. _`kvm_pmu_get_counter_value`:

kvm_pmu_get_counter_value
=========================

.. c:function:: u64 kvm_pmu_get_counter_value(struct kvm_vcpu *vcpu, u64 select_idx)

    get PMU counter value

    :param struct kvm_vcpu \*vcpu:
        The vcpu pointer

    :param u64 select_idx:
        The counter index

.. _`kvm_pmu_set_counter_value`:

kvm_pmu_set_counter_value
=========================

.. c:function:: void kvm_pmu_set_counter_value(struct kvm_vcpu *vcpu, u64 select_idx, u64 val)

    set PMU counter value

    :param struct kvm_vcpu \*vcpu:
        The vcpu pointer

    :param u64 select_idx:
        The counter index

    :param u64 val:
        The counter value

.. _`kvm_pmu_stop_counter`:

kvm_pmu_stop_counter
====================

.. c:function:: void kvm_pmu_stop_counter(struct kvm_vcpu *vcpu, struct kvm_pmc *pmc)

    stop PMU counter

    :param struct kvm_vcpu \*vcpu:
        *undescribed*

    :param struct kvm_pmc \*pmc:
        The PMU counter pointer

.. _`kvm_pmu_stop_counter.description`:

Description
-----------

If this counter has been configured to monitor some event, release it here.

.. _`kvm_pmu_vcpu_reset`:

kvm_pmu_vcpu_reset
==================

.. c:function:: void kvm_pmu_vcpu_reset(struct kvm_vcpu *vcpu)

    reset pmu state for cpu

    :param struct kvm_vcpu \*vcpu:
        The vcpu pointer

.. _`kvm_pmu_vcpu_destroy`:

kvm_pmu_vcpu_destroy
====================

.. c:function:: void kvm_pmu_vcpu_destroy(struct kvm_vcpu *vcpu)

    free perf event of PMU for cpu

    :param struct kvm_vcpu \*vcpu:
        The vcpu pointer

.. _`kvm_pmu_enable_counter`:

kvm_pmu_enable_counter
======================

.. c:function:: void kvm_pmu_enable_counter(struct kvm_vcpu *vcpu, u64 val)

    enable selected PMU counter

    :param struct kvm_vcpu \*vcpu:
        The vcpu pointer

    :param u64 val:
        the value guest writes to PMCNTENSET register

.. _`kvm_pmu_enable_counter.description`:

Description
-----------

Call perf_event_enable to start counting the perf event

.. _`kvm_pmu_disable_counter`:

kvm_pmu_disable_counter
=======================

.. c:function:: void kvm_pmu_disable_counter(struct kvm_vcpu *vcpu, u64 val)

    disable selected PMU counter

    :param struct kvm_vcpu \*vcpu:
        The vcpu pointer

    :param u64 val:
        the value guest writes to PMCNTENCLR register

.. _`kvm_pmu_disable_counter.description`:

Description
-----------

Call perf_event_disable to stop counting the perf event

.. _`kvm_pmu_overflow_set`:

kvm_pmu_overflow_set
====================

.. c:function:: void kvm_pmu_overflow_set(struct kvm_vcpu *vcpu, u64 val)

    set PMU overflow interrupt

    :param struct kvm_vcpu \*vcpu:
        The vcpu pointer

    :param u64 val:
        the value guest writes to PMOVSSET register

.. _`kvm_pmu_flush_hwstate`:

kvm_pmu_flush_hwstate
=====================

.. c:function:: void kvm_pmu_flush_hwstate(struct kvm_vcpu *vcpu)

    flush pmu state to cpu

    :param struct kvm_vcpu \*vcpu:
        The vcpu pointer

.. _`kvm_pmu_flush_hwstate.description`:

Description
-----------

Check if the PMU has overflowed while we were running in the host, and inject
an interrupt if that was the case.

.. _`kvm_pmu_sync_hwstate`:

kvm_pmu_sync_hwstate
====================

.. c:function:: void kvm_pmu_sync_hwstate(struct kvm_vcpu *vcpu)

    sync pmu state from cpu

    :param struct kvm_vcpu \*vcpu:
        The vcpu pointer

.. _`kvm_pmu_sync_hwstate.description`:

Description
-----------

Check if the PMU has overflowed while we were running in the guest, and
inject an interrupt if that was the case.

.. _`kvm_pmu_perf_overflow`:

kvm_pmu_perf_overflow
=====================

.. c:function:: void kvm_pmu_perf_overflow(struct perf_event *perf_event, struct perf_sample_data *data, struct pt_regs *regs)

    :param struct perf_event \*perf_event:
        *undescribed*

    :param struct perf_sample_data \*data:
        *undescribed*

    :param struct pt_regs \*regs:
        *undescribed*

.. _`kvm_pmu_software_increment`:

kvm_pmu_software_increment
==========================

.. c:function:: void kvm_pmu_software_increment(struct kvm_vcpu *vcpu, u64 val)

    do software increment

    :param struct kvm_vcpu \*vcpu:
        The vcpu pointer

    :param u64 val:
        the value guest writes to PMSWINC register

.. _`kvm_pmu_handle_pmcr`:

kvm_pmu_handle_pmcr
===================

.. c:function:: void kvm_pmu_handle_pmcr(struct kvm_vcpu *vcpu, u64 val)

    handle PMCR register

    :param struct kvm_vcpu \*vcpu:
        The vcpu pointer

    :param u64 val:
        the value guest writes to PMCR register

.. _`kvm_pmu_set_counter_event_type`:

kvm_pmu_set_counter_event_type
==============================

.. c:function:: void kvm_pmu_set_counter_event_type(struct kvm_vcpu *vcpu, u64 data, u64 select_idx)

    set selected counter to monitor some event

    :param struct kvm_vcpu \*vcpu:
        The vcpu pointer

    :param u64 data:
        The data guest writes to PMXEVTYPER_EL0

    :param u64 select_idx:
        The number of selected counter

.. _`kvm_pmu_set_counter_event_type.description`:

Description
-----------

When OS accesses PMXEVTYPER_EL0, that means it wants to set a PMC to count an
event with given hardware event number. Here we call perf_event API to
emulate this action and create a kernel perf event for it.

.. This file was automatic generated / don't edit.

