.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/sched/fair.c

.. _`update_tg_load_avg`:

update_tg_load_avg
==================

.. c:function:: void update_tg_load_avg(struct cfs_rq *cfs_rq, int force)

    update the tg's load avg

    :param struct cfs_rq \*cfs_rq:
        the cfs_rq whose avg changed

    :param int force:
        update regardless of how small the difference

.. _`update_tg_load_avg.description`:

Description
-----------

This function 'ensures': tg->load_avg := \Sum tg->cfs_rq[]->avg.load.
However, because tg->load_avg is a global value there are performance
considerations.

In order to avoid having to look at the other cfs_rq's, we use a
differential update where we store the last value we propagated. This in
turn allows skipping updates if the differential is 'small'.

Updating tg's load_avg is necessary before \ :c:func:`update_cfs_share`\ .

.. _`update_cfs_rq_load_avg`:

update_cfs_rq_load_avg
======================

.. c:function:: int update_cfs_rq_load_avg(u64 now, struct cfs_rq *cfs_rq)

    update the cfs_rq's load/util averages

    :param u64 now:
        current time, as per \ :c:func:`cfs_rq_clock_task`\ 

    :param struct cfs_rq \*cfs_rq:
        cfs_rq to update

.. _`update_cfs_rq_load_avg.description`:

Description
-----------

The cfs_rq avg is the direct sum of all its entities (blocked and runnable)
avg. The immediate corollary is that all (fair) tasks must be attached, see
\ :c:func:`post_init_entity_util_avg`\ .

cfs_rq->avg is used for \ :c:func:`task_h_load`\  and \ :c:func:`update_cfs_share`\  for example.

Returns true if the load decayed or we removed load.

Since both these conditions indicate a changed cfs_rq->avg.load we should
call \ :c:func:`update_tg_load_avg`\  when this function returns true.

.. _`attach_entity_load_avg`:

attach_entity_load_avg
======================

.. c:function:: void attach_entity_load_avg(struct cfs_rq *cfs_rq, struct sched_entity *se)

    attach this entity to its cfs_rq load avg

    :param struct cfs_rq \*cfs_rq:
        cfs_rq to attach to

    :param struct sched_entity \*se:
        sched_entity to attach

.. _`attach_entity_load_avg.description`:

Description
-----------

Must call \ :c:func:`update_cfs_rq_load_avg`\  before this, since we rely on
cfs_rq->avg.last_update_time being current.

.. _`detach_entity_load_avg`:

detach_entity_load_avg
======================

.. c:function:: void detach_entity_load_avg(struct cfs_rq *cfs_rq, struct sched_entity *se)

    detach this entity from its cfs_rq load avg

    :param struct cfs_rq \*cfs_rq:
        cfs_rq to detach from

    :param struct sched_entity \*se:
        sched_entity to detach

.. _`detach_entity_load_avg.description`:

Description
-----------

Must call \ :c:func:`update_cfs_rq_load_avg`\  before this, since we rely on
cfs_rq->avg.last_update_time being current.

.. _`cpu_load_update`:

cpu_load_update
===============

.. c:function:: void cpu_load_update(struct rq *this_rq, unsigned long this_load, unsigned long pending_updates)

    update the rq->cpu_load[] statistics

    :param struct rq \*this_rq:
        The rq to update statistics for

    :param unsigned long this_load:
        The current load

    :param unsigned long pending_updates:
        The number of missed updates

.. _`cpu_load_update.description`:

Description
-----------

Update rq->cpu_load[] statistics. This function is usually called every
scheduler tick (TICK_NSEC).

.. _`cpu_load_update.this-function-computes-a-decaying-average`:

This function computes a decaying average
-----------------------------------------


  load[i]' = (1 - 1/2^i) * load[i] + (1/2^i) * load

Because of NOHZ it might not get called on every tick which gives need for
the \ ``pending_updates``\  argument.

  load[i]_n = (1 - 1/2^i) * load[i]_n-1 + (1/2^i) * load_n-1
            = A * load[i]_n-1 + B ; A := (1 - 1/2^i), B := (1/2^i) * load
            = A * (A * load[i]_n-2 + B) + B
            = A * (A * (A * load[i]_n-3 + B) + B) + B
            = A^3 * load[i]_n-3 + (A^2 + A + 1) * B
            = A^n * load[i]_0 + (A^(n-1) + A^(n-2) + ... + 1) * B
            = A^n * load[i]_0 + ((1 - A^n) / (1 - A)) * B
            = (1 - 1/2^i)^n * (load[i]_0 - load) + load

In the above we've assumed load_n := load, which is true for NOHZ_FULL as
any change in load would have resulted in the tick being turned back on.

For regular NOHZ, this reduces to:

  load[i]_n = (1 - 1/2^i)^n * load[i]_0

see \ :c:func:`decay_load_misses`\ . For NOHZ_FULL we get to subtract and add the extra
term.

.. _`get_sd_load_idx`:

get_sd_load_idx
===============

.. c:function:: int get_sd_load_idx(struct sched_domain *sd, enum cpu_idle_type idle)

    Obtain the load index for a given sched domain.

    :param struct sched_domain \*sd:
        The sched_domain whose load_idx is to be obtained.

    :param enum cpu_idle_type idle:
        The idle status of the CPU for whose sd load_idx is obtained.

.. _`get_sd_load_idx.return`:

Return
------

The load index.

.. _`update_sg_lb_stats`:

update_sg_lb_stats
==================

.. c:function:: void update_sg_lb_stats(struct lb_env *env, struct sched_group *group, int load_idx, int local_group, struct sg_lb_stats *sgs, bool *overload)

    Update sched_group's statistics for load balancing.

    :param struct lb_env \*env:
        The load balancing environment.

    :param struct sched_group \*group:
        sched_group whose statistics are to be updated.

    :param int load_idx:
        Load index of sched_domain of this_cpu for load calc.

    :param int local_group:
        Does group contain this_cpu.

    :param struct sg_lb_stats \*sgs:
        variable to hold the statistics for this group.

    :param bool \*overload:
        Indicate more than one runnable task for any CPU.

.. _`update_sd_pick_busiest`:

update_sd_pick_busiest
======================

.. c:function:: bool update_sd_pick_busiest(struct lb_env *env, struct sd_lb_stats *sds, struct sched_group *sg, struct sg_lb_stats *sgs)

    return 1 on busiest group

    :param struct lb_env \*env:
        The load balancing environment.

    :param struct sd_lb_stats \*sds:
        sched_domain statistics

    :param struct sched_group \*sg:
        sched_group candidate to be checked for being the busiest

    :param struct sg_lb_stats \*sgs:
        sched_group statistics

.. _`update_sd_pick_busiest.description`:

Description
-----------

Determine if \ ``sg``\  is a busier group than the previously selected
busiest group.

.. _`update_sd_pick_busiest.return`:

Return
------

%true if \ ``sg``\  is a busier group than the previously selected
busiest group. \ ``false``\  otherwise.

.. _`update_sd_lb_stats`:

update_sd_lb_stats
==================

.. c:function:: void update_sd_lb_stats(struct lb_env *env, struct sd_lb_stats *sds)

    Update sched_domain's statistics for load balancing.

    :param struct lb_env \*env:
        The load balancing environment.

    :param struct sd_lb_stats \*sds:
        variable to hold the statistics for this sched_domain.

.. _`check_asym_packing`:

check_asym_packing
==================

.. c:function:: int check_asym_packing(struct lb_env *env, struct sd_lb_stats *sds)

    Check to see if the group is packed into the sched domain.

    :param struct lb_env \*env:
        The load balancing environment.

    :param struct sd_lb_stats \*sds:
        Statistics of the sched_domain which is to be packed

.. _`check_asym_packing.description`:

Description
-----------

This is primarily intended to used at the sibling level.  Some
cores like POWER7 prefer to use lower numbered SMT threads.  In the
case of POWER7, it can move to lower SMT modes only when higher
threads are idle.  When in lower SMT modes, the threads will
perform better since they share less core resources.  Hence when we
have idle threads, we want them to be the higher ones.

This packing function is run on idle threads.  It checks to see if
the busiest CPU in this domain (core in the P7 case) has a higher
CPU number than the packing function is being run on.  Here we are
assuming lower CPU number will be equivalent to lower a SMT thread
number.

.. _`check_asym_packing.return`:

Return
------

1 when packing is required and a task should be moved to
this CPU.  The amount of the imbalance is returned in env->imbalance.

.. _`fix_small_imbalance`:

fix_small_imbalance
===================

.. c:function:: void fix_small_imbalance(struct lb_env *env, struct sd_lb_stats *sds)

    Calculate the minor imbalance that exists amongst the groups of a sched_domain, during load balancing.

    :param struct lb_env \*env:
        The load balancing environment.

    :param struct sd_lb_stats \*sds:
        Statistics of the sched_domain whose imbalance is to be calculated.

.. _`calculate_imbalance`:

calculate_imbalance
===================

.. c:function:: void calculate_imbalance(struct lb_env *env, struct sd_lb_stats *sds)

    Calculate the amount of imbalance present within the groups of a given sched_domain during load balance.

    :param struct lb_env \*env:
        load balance environment

    :param struct sd_lb_stats \*sds:
        statistics of the sched_domain whose imbalance is to be calculated.

.. _`find_busiest_group`:

find_busiest_group
==================

.. c:function:: struct sched_group *find_busiest_group(struct lb_env *env)

    Returns the busiest group within the sched_domain if there is an imbalance.

    :param struct lb_env \*env:
        The load balancing environment.

.. _`find_busiest_group.description`:

Description
-----------

Also calculates the amount of weighted load which should be moved
to restore balance.

.. _`find_busiest_group.return`:

Return
------

- The busiest group if imbalance exists.

.. This file was automatic generated / don't edit.

