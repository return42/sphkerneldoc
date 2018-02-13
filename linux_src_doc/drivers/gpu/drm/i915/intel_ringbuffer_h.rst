.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/intel_ringbuffer.h

.. _`intel_engine_execlists`:

struct intel_engine_execlists
=============================

.. c:type:: struct intel_engine_execlists

    execlist submission queue and port state

.. _`intel_engine_execlists.definition`:

Definition
----------

.. code-block:: c

    struct intel_engine_execlists {
        struct tasklet_struct tasklet;
        struct i915_priolist default_priolist;
        bool no_priolist;
        u32 __iomem *elsp;
        struct execlist_port {
            struct drm_i915_gem_request *request_count;
    #define EXECLIST_COUNT_BITS 2
    #define port_request(p) ptr_mask_bits((p)->request_count, EXECLIST_COUNT_BITS)
    #define port_count(p) ptr_unmask_bits((p)->request_count, EXECLIST_COUNT_BITS)
    #define port_pack(rq, count) ptr_pack_bits(rq, count, EXECLIST_COUNT_BITS)
    #define port_unpack(p, count) ptr_unpack_bits((p)->request_count, count, EXECLIST_COUNT_BITS)
    #define port_set(p, packed) ((p)->request_count = (packed))
    #define port_isset(p) ((p)->request_count)
    #define port_index(p, execlists) ((p) - (execlists)->port)
            GEM_DEBUG_DECL(u32 context_id);
    #define EXECLIST_MAX_PORTS 2
        } port[EXECLIST_MAX_PORTS];
        unsigned int active;
    #define EXECLISTS_ACTIVE_USER 0
    #define EXECLISTS_ACTIVE_PREEMPT 1
    #define EXECLISTS_ACTIVE_HWACK 2
        unsigned int port_mask;
        struct rb_root queue;
        struct rb_node *first;
        unsigned int fw_domains;
        unsigned int csb_head;
        bool csb_use_mmio;
    }

.. _`intel_engine_execlists.members`:

Members
-------

tasklet
    softirq tasklet for bottom handler

default_priolist
    priority list for I915_PRIORITY_NORMAL

no_priolist
    priority lists disabled

elsp
    the ExecList Submission Port register

port
    execlist port states
    For each hardware ELSP (ExecList Submission Port) we keep
    track of the last request and the number of times we submitted
    that port to hw. We then count the number of times the hw reports
    a context completion or preemption. As only one context can
    be active on hw, we limit resubmission of context to port[0]. This
    is called Lite Restore, of the context.

active
    is the HW active? We consider the HW as active aftersubmitting any context for execution and until we have seen the
    last context completion event. After that, we do not expect any
    more events until we submit, and so can park the HW.

    As we have a small number of different sources from which we feed
    the HW, we track the state of each inside a single bitfield.

port_mask
    number of execlist ports - 1

queue
    queue of requests, in priority lists

first
    leftmost level in priority \ ``queue``\ 

fw_domains
    forcewake domains for irq tasklet

csb_head
    context status buffer head

csb_use_mmio
    access csb through mmio, instead of hwsp

.. _`intel_engine_execlists.description`:

Description
-----------

The struct intel_engine_execlists represents the combined logical state of
driver and the hardware state for execlist mode of submission.

.. This file was automatic generated / don't edit.

