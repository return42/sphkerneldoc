.. -*- coding: utf-8; mode: rst -*-

.. _Basics:

=============
Driver Basics
=============


Driver Entry and Exit points
============================


.. toctree::
    :maxdepth: 1

    Basics-000-001-002


Atomic and pointer manipulation
===============================


.. toctree::
    :maxdepth: 1

    API-atomic-read
    API-atomic-set
    API-atomic-add
    API-atomic-sub
    API-atomic-sub-and-test
    API-atomic-inc
    API-atomic-dec
    API-atomic-dec-and-test
    API-atomic-inc-and-test
    API-atomic-add-negative
    API-atomic-add-return
    API-atomic-sub-return
    API---atomic-add-unless
    API-atomic-inc-short


Delaying, scheduling, and timer routines
========================================


.. toctree::
    :maxdepth: 1

    API-struct-prev-cputime
    API-struct-task-cputime
    API-struct-thread-group-cputimer
    API-pid-alive
    API-is-global-init
    API-task-nice
    API-is-idle-task
    API-threadgroup-change-begin
    API-threadgroup-change-end
    API-wake-up-process
    API-preempt-notifier-register
    API-preempt-notifier-unregister
    API-preempt-schedule-notrace
    API-sched-setscheduler
    API-sched-setscheduler-nocheck
    API-yield
    API-yield-to
    API-cpupri-find
    API-cpupri-set
    API-cpupri-init
    API-cpupri-cleanup
    API---update-cpu-load
    API-get-sd-load-idx
    API-update-sg-lb-stats
    API-update-sd-pick-busiest
    API-update-sd-lb-stats
    API-check-asym-packing
    API-fix-small-imbalance
    API-calculate-imbalance
    API-find-busiest-group
    API-DECLARE-COMPLETION
    API-DECLARE-COMPLETION-ONSTACK
    API-init-completion
    API-reinit-completion
    API---round-jiffies
    API---round-jiffies-relative
    API-round-jiffies
    API-round-jiffies-relative
    API---round-jiffies-up
    API---round-jiffies-up-relative
    API-round-jiffies-up
    API-round-jiffies-up-relative
    API-set-timer-slack
    API-init-timer-key
    API-mod-timer-pending
    API-mod-timer
    API-mod-timer-pinned
    API-add-timer
    API-add-timer-on
    API-del-timer
    API-try-to-del-timer-sync
    API-del-timer-sync
    API-schedule-timeout
    API-msleep
    API-msleep-interruptible
    API-usleep-range


Wait queues and Wake events
===========================


.. toctree::
    :maxdepth: 1

    API-waitqueue-active
    API-wq-has-sleeper
    API-wait-event
    API-wait-event-freezable
    API-wait-event-timeout
    API-wait-event-cmd
    API-wait-event-interruptible
    API-wait-event-interruptible-timeout
    API-wait-event-hrtimeout
    API-wait-event-interruptible-hrtimeout
    API-wait-event-interruptible-locked
    API-wait-event-interruptible-locked-irq
    API-wait-event-interruptible-exclusive-locked
    API-wait-event-interruptible-exclusive-locked-irq
    API-wait-event-killable
    API-wait-event-lock-irq-cmd
    API-wait-event-lock-irq
    API-wait-event-interruptible-lock-irq-cmd
    API-wait-event-interruptible-lock-irq
    API-wait-event-interruptible-lock-irq-timeout
    API-wait-on-bit
    API-wait-on-bit-io
    API-wait-on-bit-timeout
    API-wait-on-bit-action
    API-wait-on-bit-lock
    API-wait-on-bit-lock-io
    API-wait-on-bit-lock-action
    API-wait-on-atomic-t
    API---wake-up
    API---wake-up-sync-key
    API-finish-wait
    API-abort-exclusive-wait
    API-wake-up-bit
    API-wake-up-atomic-t


High-resolution timers
======================


.. toctree::
    :maxdepth: 1

    API-ktime-set
    API-ktime-equal
    API-ktime-compare
    API-ktime-after
    API-ktime-before
    API-ktime-to-timespec-cond
    API-ktime-to-timespec64-cond
    API-struct-hrtimer
    API-struct-hrtimer-sleeper
    API-struct-hrtimer-clock-base
    API-hrtimer-start
    API-hrtimer-forward-now
    API-hrtimer-forward
    API-hrtimer-start-range-ns
    API-hrtimer-try-to-cancel
    API-hrtimer-cancel
    API---hrtimer-get-remaining
    API-hrtimer-init
    API-schedule-hrtimeout-range
    API-schedule-hrtimeout


Workqueues and Kevents
======================


.. toctree::
    :maxdepth: 1

    API-work-pending
    API-delayed-work-pending
    API-alloc-workqueue
    API-alloc-ordered-workqueue
    API-queue-work
    API-queue-delayed-work
    API-mod-delayed-work
    API-schedule-work-on
    API-schedule-work
    API-flush-scheduled-work
    API-schedule-delayed-work-on
    API-schedule-delayed-work
    API-keventd-up
    API-queue-work-on
    API-queue-delayed-work-on
    API-mod-delayed-work-on
    API-flush-workqueue
    API-drain-workqueue
    API-flush-work
    API-cancel-work-sync
    API-flush-delayed-work
    API-cancel-delayed-work
    API-cancel-delayed-work-sync
    API-execute-in-process-context
    API-destroy-workqueue
    API-workqueue-set-max-active
    API-workqueue-congested
    API-work-busy
    API-work-on-cpu


Internal Functions
==================


.. toctree::
    :maxdepth: 1

    API-wait-task-stopped
    API-task-set-jobctl-pending
    API-task-clear-jobctl-trapping
    API-task-clear-jobctl-pending
    API-task-participate-group-stop
    API-ptrace-trap-notify
    API-do-notify-parent-cldstop
    API-do-signal-stop
    API-do-jobctl-trap
    API-signal-delivered
    API-sys-restart-syscall
    API-set-current-blocked
    API-sys-rt-sigprocmask
    API-sys-rt-sigpending
    API-do-sigtimedwait
    API-sys-rt-sigtimedwait
    API-sys-kill
    API-sys-tgkill
    API-sys-tkill
    API-sys-rt-sigqueueinfo
    API-sys-sigpending
    API-sys-sigprocmask
    API-sys-rt-sigaction
    API-sys-rt-sigsuspend
    API-kthread-run
    API-kthread-should-stop
    API-kthread-should-park
    API-kthread-freezable-should-stop
    API-kthread-create-on-node
    API-kthread-bind
    API-kthread-unpark
    API-kthread-park
    API-kthread-stop
    API-kthread-worker-fn
    API-queue-kthread-work
    API-flush-kthread-work
    API-flush-kthread-worker


Kernel objects manipulation
===========================


.. toctree::
    :maxdepth: 1

    API-kobject-get-path
    API-kobject-set-name
    API-kobject-init
    API-kobject-add
    API-kobject-init-and-add
    API-kobject-rename
    API-kobject-move
    API-kobject-del
    API-kobject-get
    API-kobject-put
    API-kobject-create-and-add
    API-kset-register
    API-kset-unregister
    API-kset-find-obj
    API-kset-create-and-add


Kernel utility functions
========================


.. toctree::
    :maxdepth: 1

    API-upper-32-bits
    API-lower-32-bits
    API-might-sleep
    API-abs
    API-reciprocal-scale
    API-kstrtoul
    API-kstrtol
    API-trace-printk
    API-trace-puts
    API-min-not-zero
    API-clamp
    API-clamp-t
    API-clamp-val
    API-container-of
    API-printk
    API-console-lock
    API-console-trylock
    API-console-unlock
    API-console-conditional-schedule
    API-printk-timed-ratelimit
    API-kmsg-dump-register
    API-kmsg-dump-unregister
    API-kmsg-dump-get-line
    API-kmsg-dump-get-buffer
    API-kmsg-dump-rewind
    API-panic
    API-add-taint
    Basics-000-009-032
    API-init-srcu-struct
    API-cleanup-srcu-struct
    API-synchronize-srcu
    API-synchronize-srcu-expedited
    API-srcu-barrier
    API-srcu-batches-completed
    API-rcu-idle-enter
    API-rcu-idle-exit
    API-rcu-is-watching
    API-synchronize-sched
    API-synchronize-rcu-bh
    API-get-state-synchronize-rcu
    API-cond-synchronize-rcu
    API-get-state-synchronize-sched
    API-cond-synchronize-sched
    API-synchronize-sched-expedited
    API-rcu-barrier-bh
    API-rcu-barrier-sched
    API-synchronize-rcu
    API-synchronize-rcu-expedited
    API-rcu-barrier
    API-rcu-read-lock-sched-held
    API-rcu-expedite-gp
    API-rcu-unexpedite-gp
    API-rcu-read-lock-held
    API-rcu-read-lock-bh-held
    API-wakeme-after-rcu
    API-init-rcu-head-on-stack
    API-destroy-rcu-head-on-stack
    API-synchronize-rcu-tasks
    API-rcu-barrier-tasks


Device Resource Management
==========================


.. toctree::
    :maxdepth: 1

    API-devres-alloc-node
    API-devres-for-each-res
    API-devres-free
    API-devres-add
    API-devres-find
    API-devres-get
    API-devres-remove
    API-devres-destroy
    API-devres-release
    API-devres-open-group
    API-devres-close-group
    API-devres-remove-group
    API-devres-release-group
    API-devm-add-action
    API-devm-remove-action
    API-devm-kmalloc
    API-devm-kstrdup
    API-devm-kvasprintf
    API-devm-kasprintf
    API-devm-kfree
    API-devm-kmemdup
    API-devm-get-free-pages
    API-devm-free-pages




.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
