
.. _drmI915:

=========================
drm/i915 Intel GFX Driver
=========================

The drm/i915 driver supports all (with the exception of some very early models) integrated GFX chipsets with both Intel display and rendering blocks. This excludes a set of SoC
platforms with an SGX rendering unit, those have basic support through the gma500 drm driver.


Core Driver Infrastructure
==========================

This section covers core driver infrastructure used by both the display and the GEM parts of the driver.


Runtime Power Management
------------------------

The i915 driver supports dynamic enabling and disabling of entire hardware blocks at runtime. This is especially important on the display side where software is supposed to control
many power gates manually on recent hardware, since on the GT side a lot of the power management is done by the hardware. But even there some manual control at the device level is
required.

Since i915 supports a diverse set of platforms with a unified codebase and hardware engineers just love to shuffle functionality around between power domains there's a sizeable
amount of indirection required. This file provides generic functions to the driver for grabbing and releasing references for abstract power domains. It then maps those to the
actual power wells present for a given platform.


.. toctree::
    :maxdepth: 1

    API---intel-display-power-is-enabled
    API-intel-display-power-is-enabled
    API-intel-display-set-init-power
    API-intel-display-power-get
    API-intel-display-power-get-if-enabled
    API-intel-display-power-put
    API-intel-power-domains-init
    API-intel-power-domains-fini
    API-intel-power-domains-init-hw
    API-intel-power-domains-suspend
    API-intel-runtime-pm-get
    API-intel-runtime-pm-get-if-in-use
    API-intel-runtime-pm-get-noresume
    API-intel-runtime-pm-put
    API-intel-runtime-pm-enable
    API-intel-uncore-forcewake-get
    API-intel-uncore-forcewake-get--locked
    API-intel-uncore-forcewake-put
    API-intel-uncore-forcewake-put--locked

Interrupt Handling
------------------

These functions provide the basic support for enabling and disabling the interrupt handling support. There's a lot more functionality in i915_irq.c and related files, but that
will be described in separate chapters.


.. toctree::
    :maxdepth: 1

    API-intel-irq-init
    API-intel-runtime-pm-disable-interrupts
    API-intel-runtime-pm-enable-interrupts

Intel GVT-g Guest Support(vGPU)
-------------------------------

Intel GVT-g is a graphics virtualization technology which shares the GPU among multiple virtual machines on a time-sharing basis. Each virtual machine is presented a virtual GPU
(vGPU), which has equivalent features as the underlying physical GPU (pGPU), so i915 driver can run seamlessly in a virtual machine. This file provides vGPU specific optimizations
when running in a virtual machine, to reduce the complexity of vGPU emulation and to improve the overall performance.

A primary function introduced here is so-called “address space ballooning” technique. Intel GVT-g partitions global graphics memory among multiple VMs, so each VM can directly
access a portion of the memory without hypervisor's intervention, e.g. filling textures or queuing commands. However with the partitioning an unmodified i915 driver would assume a
smaller graphics memory starting from address ZERO, then requires vGPU emulation module to translate the graphics address between 'guest view' and 'host view', for all registers
and command opcodes which contain a graphics memory address. To reduce the complexity, Intel GVT-g introduces “address space ballooning”, by telling the exact partitioning
knowledge to each guest i915 driver, which then reserves and prevents non-allocated portions from allocation. Thus vGPU emulation module only needs to scan and validate graphics
addresses without complexity of address translation.


.. toctree::
    :maxdepth: 1

    API-i915-check-vgpu
    API-intel-vgt-deballoon
    API-intel-vgt-balloon

Display Hardware Handling
=========================

This section covers everything related to the display hardware including the mode setting infrastructure, plane, sprite and cursor handling and display, output probing and related
topics.


Mode Setting Infrastructure
---------------------------

The i915 driver is thus far the only DRM driver which doesn't use the common DRM helper code to implement mode setting sequences. Thus it has its own tailor-made infrastructure for
executing a display configuration change.


Frontbuffer Tracking
--------------------

Many features require us to track changes to the currently active frontbuffer, especially rendering targeted at the frontbuffer.

To be able to do so GEM tracks frontbuffers using a bitmask for all possible frontbuffer slots through ``i915_gem_track_fb``. The function in this file are then called when the
contents of the frontbuffer are invalidated, when frontbuffer rendering has stopped again to flush out all the changes and when the frontbuffer is exchanged with a flip. Subsystems
interested in frontbuffer changes (e.g. PSR, FBC, DRRS) should directly put their callbacks into the relevant places and filter for the frontbuffer slots that they are interested
int.

On a high level there are two types of powersaving features. The first one work like a special cache (FBC and PSR) and are interested when they should stop caching and when to
restart caching. This is done by placing callbacks into the invalidate and the flush functions: At invalidate the caching must be stopped and at flush time it can be restarted. And
maybe they need to know when the frontbuffer changes (e.g. when the hw doesn't initiate an invalidate and flush on its own) which can be achieved with placing callbacks into the
flip functions.

The other type of display power saving feature only cares about busyness (e.g. DRRS). In that case all three (invalidate, flush and flip) indicate busyness. There is no direct way
to detect idleness. Instead an idle timer work delayed work should be started from the flush and flip functions and cancelled as soon as busyness is detected.

Note that there's also an older frontbuffer activity tracking scheme which just tracks general activity. This is done by the various mark_busy and mark_idle functions. For
display power management features using these functions is deprecated and should be avoided.


.. toctree::
    :maxdepth: 1

    API-intel-fb-obj-invalidate
    API-intel-frontbuffer-flush
    API-intel-fb-obj-flush
    API-intel-frontbuffer-flip-prepare
    API-intel-frontbuffer-flip-complete
    API-intel-frontbuffer-flip
    API-i915-gem-track-fb

Display FIFO Underrun Reporting
-------------------------------

The i915 driver checks for display fifo underruns using the interrupt signals provided by the hardware. This is enabled by default and fairly useful to debug display issues,
especially watermark settings.

If an underrun is detected this is logged into dmesg. To avoid flooding logs and occupying the cpu underrun interrupts are disabled after the first occurrence until the next
modeset on a given pipe.

Note that underrun detection on gmch platforms is a bit more ugly since there is no interrupt (despite that the signalling bit is in the PIPESTAT pipe interrupt register). Also on
some other platforms underrun interrupts are shared, which means that if we detect an underrun we need to disable underrun reporting on all pipes.

The code also supports underrun detection on the PCH transcoder.


.. toctree::
    :maxdepth: 1

    API-intel-set-cpu-fifo-underrun-reporting
    API-intel-set-pch-fifo-underrun-reporting
    API-intel-cpu-fifo-underrun-irq-handler
    API-intel-pch-fifo-underrun-irq-handler
    API-intel-check-cpu-fifo-underruns
    API-intel-check-pch-fifo-underruns

Plane Configuration
-------------------

This section covers plane configuration and composition with the primary plane, sprites, cursors and overlays. This includes the infrastructure to do atomic vsync'ed updates of all
this state and also tightly coupled topics like watermark setup and computation, framebuffer compression and panel self refresh.


Atomic Plane Helpers
--------------------

The functions here are used by the atomic plane helper functions to implement legacy plane updates (i.e., drm_plane-> ``update_plane`` and drm_plane-> ``disable_plane``). This
allows plane updates to use the atomic state infrastructure and perform plane updates as separate prepare/check/commit/cleanup steps.


.. toctree::
    :maxdepth: 1

    API-intel-create-plane-state
    API-intel-plane-duplicate-state
    API-intel-plane-destroy-state
    API-intel-plane-atomic-get-property
    API-intel-plane-atomic-set-property

Output Probing
--------------

This section covers output probing and related infrastructure like the hotplug interrupt storm detection and mitigation code. Note that the i915 driver still uses most of the
common DRM helper code for output probing, so those sections fully apply.


Hotplug
-------

Simply put, hotplug occurs when a display is connected to or disconnected from the system. However, there may be adapters and docking stations and Display Port short pulses and MST
devices involved, complicating matters.

Hotplug in i915 is handled in many different levels of abstraction.

The platform dependent interrupt handling code in i915_irq.c enables, disables, and does preliminary handling of the interrupts. The interrupt handlers gather the hotplug detect
(HPD) information from relevant registers into a platform independent mask of hotplug pins that have fired.

The platform independent interrupt handler ``intel_hpd_irq_handler`` in intel_hotplug.c does hotplug irq storm detection and mitigation, and passes further processing to
appropriate bottom halves (Display Port specific and regular hotplug).

The Display Port work function ``i915_digport_work_func`` calls into ``intel_dp_hpd_pulse`` via hooks, which handles DP short pulses and DP MST long pulses, with failures and
non-MST long pulses triggering regular hotplug processing on the connector.

The regular hotplug work function ``i915_hotplug_work_func`` calls connector detect hooks, and, if connector status changes, triggers sending of hotplug uevent to userspace via
``drm_kms_helper_hotplug_event``.

Finally, the userspace is responsible for triggering a modeset upon receiving the hotplug uevent, disabling or enabling the crtc as needed.

The hotplug interrupt storm detection and mitigation code keeps track of the number of interrupts per hotplug pin per a period of time, and if the number of interrupts exceeds a
certain threshold, the interrupt is disabled for a while before being re-enabled. The intention is to mitigate issues raising from broken hardware triggering massive amounts of
interrupts and grinding the system to a halt.

Current implementation expects that hotplug interrupt storm will not be seen when display port sink is connected, hence on platforms whose DP callback is handled by
i915_digport_work_func reenabling of hpd is not performed (it was never expected to be disabled in the first place ;) ) this is specific to DP sinks handled by this routine and
any other display such as HDMI or DVI enabled on the same port will have proper logic since it will use i915_hotplug_work_func where this logic is handled.


.. toctree::
    :maxdepth: 1

    API-intel-hpd-irq-storm-detect
    API-intel-hpd-irq-handler
    API-intel-hpd-init

High Definition Audio
---------------------

The graphics and audio drivers together support High Definition Audio over HDMI and Display Port. The audio programming sequences are divided into audio codec and controller enable
and disable sequences. The graphics driver handles the audio codec sequences, while the audio driver handles the audio controller sequences.

The disable sequences must be performed before disabling the transcoder or port. The enable sequences may only be performed after enabling the transcoder and port, and after
completed link training. Therefore the audio enable/disable sequences are part of the modeset sequence.

The codec and controller sequences could be done either parallel or serial, but generally the ELDV/PD change in the codec sequence indicates to the audio driver that the controller
sequence should start. Indeed, most of the co-operation between the graphics and audio drivers is handled via audio related registers. (The notable exception is the power
management, not covered here.)

The struct i915_audio_component is used to interact between the graphics and audio drivers. The struct i915_audio_component_ops ⋆ops in it is defined in graphics driver and
called in audio driver. The struct i915_audio_component_audio_ops ⋆audio_ops is called from i915 driver.


.. toctree::
    :maxdepth: 1

    API-intel-audio-codec-enable
    API-intel-audio-codec-disable
    API-intel-init-audio
    API-i915-audio-component-init
    API-i915-audio-component-cleanup
    API-struct-i915-audio-component-ops
    API-struct-i915-audio-component-audio-ops
    API-struct-i915-audio-component

Panel Self Refresh PSR (PSR/SRD)
--------------------------------

Since Haswell Display controller supports Panel Self-Refresh on display panels witch have a remote frame buffer (RFB) implemented according to PSR spec in eDP1.3. PSR feature
allows the display to go to lower standby states when system is idle but display is on as it eliminates display refresh request to DDR memory completely as long as the frame buffer
for that display is unchanged.

Panel Self Refresh must be supported by both Hardware (source) and Panel (sink).

PSR saves power by caching the framebuffer in the panel RFB, which allows us to power down the link and memory controller. For DSI panels the same idea is called “manual mode”.

The implementation uses the hardware-based PSR support which automatically enters/exits self-refresh mode. The hardware takes care of sending the required DP aux message and could
even retrain the link (that part isn't enabled yet though). The hardware also keeps track of any frontbuffer changes to know when to exit self-refresh mode again. Unfortunately
that part doesn't work too well, hence why the i915 PSR support uses the software frontbuffer tracking to make sure it doesn't miss a screen update. For this integration
``intel_psr_invalidate`` and ``intel_psr_flush`` get called by the frontbuffer tracking code. Note that because of locking issues the self-refresh re-enable code is done from a
work queue, which must be correctly synchronized/cancelled when shutting down the pipe."


.. toctree::
    :maxdepth: 1

    API-intel-psr-enable
    API-intel-psr-disable
    API-intel-psr-single-frame-update
    API-intel-psr-invalidate
    API-intel-psr-flush
    API-intel-psr-init

Frame Buffer Compression (FBC)
------------------------------

FBC tries to save memory bandwidth (and so power consumption) by compressing the amount of memory used by the display. It is total transparent to user space and completely handled
in the kernel.

The benefits of FBC are mostly visible with solid backgrounds and variation-less patterns. It comes from keeping the memory footprint small and having fewer memory pages opened and
accessed for refreshing the display.

i915 is responsible to reserve stolen memory for FBC and configure its offset on proper registers. The hardware takes care of all compress/decompress. However there are many known
cases where we have to forcibly disable it to allow proper screen updates.


.. toctree::
    :maxdepth: 1

    API-intel-fbc-is-active
    API-intel-fbc-choose-crtc
    API-intel-fbc-enable
    API---intel-fbc-disable
    API-intel-fbc-disable
    API-intel-fbc-global-disable
    API-intel-fbc-init-pipe-state
    API-intel-fbc-init

Display Refresh Rate Switching (DRRS)
-------------------------------------

Display Refresh Rate Switching (DRRS) is a power conservation feature which enables swtching between low and high refresh rates, dynamically, based on the usage scenario. This
feature is applicable for internal panels.

Indication that the panel supports DRRS is given by the panel EDID, which would list multiple refresh rates for one resolution.

DRRS is of 2 types - static and seamless. Static DRRS involves changing refresh rate (RR) by doing a full modeset (may appear as a blink on screen) and is used in dock-undock
scenario. Seamless DRRS involves changing RR without any visual effect to the user and can be used during normal system usage. This is done by programming certain registers.

Support for static/seamless DRRS may be indicated in the VBT based on inputs from the panel spec.

DRRS saves power by switching to low RR based on usage scenarios.

eDP DRRS:- The implementation is based on frontbuffer tracking implementation. When there is a disturbance on the screen triggered by user activity or a periodic system activity,
DRRS is disabled (RR is changed to high RR). When there is no movement on screen, after a timeout of 1 second, a switch to low RR is made. For integration with frontbuffer tracking
code, ``intel_edp_drrs_invalidate`` and ``intel_edp_drrs_flush`` are called.

DRRS can be further extended to support other internal panels and also the scenario of video playback wherein RR is set based on the rate requested by userspace.


.. toctree::
    :maxdepth: 1

    API-intel-dp-set-drrs-state
    API-intel-edp-drrs-enable
    API-intel-edp-drrs-disable
    API-intel-edp-drrs-invalidate
    API-intel-edp-drrs-flush
    API-intel-dp-drrs-init

DPIO
----

VLV, CHV and BXT have slightly peculiar display PHYs for driving DP/HDMI ports. DPIO is the name given to such a display PHY. These PHYs don't follow the standard programming model
using direct MMIO registers, and instead their registers must be accessed trough IOSF sideband. VLV has one such PHY for driving ports B and C, and CHV adds another PHY for driving
port D. Each PHY responds to specific IOSF-SB port.

Each display PHY is made up of one or two channels. Each channel houses a common lane part which contains the PLL and other common logic. CH0 common lane also contains the IOSF-SB
logic for the Common Register Interface (CRI) ie. the DPIO registers. CRI clock must be running when any DPIO registers are accessed.

In addition to having their own registers, the PHYs are also controlled through some dedicated signals from the display controller. These include PLL reference clock enable, PLL
enable, and CRI clock selection, for example.

Eeach channel also has two splines (also called data lanes), and each spline is made up of one Physical Access Coding Sub-Layer (PCS) block and two TX lanes. So each channel has
two PCS blocks and four TX lanes. The TX lanes are used as DP lanes or TMDS data/clock pairs depending on the output type.

Additionally the PHY also contains an AUX lane with AUX blocks for each channel. This is used for DP AUX communication, but this fact isn't really relevant for the driver since AUX
is controlled from the display controller side. No DPIO registers need to be accessed during AUX communication,

Generally on VLV/CHV the common lane corresponds to the pipe and the spline (PCS/TX) corresponds to the port.

For dual channel PHY (VLV/CHV):

pipe A == CMN/PLL/REF CH0

pipe B == CMN/PLL/REF CH1

port B == PCS/TX CH0

port C == PCS/TX CH1

This is especially important when we cross the streams ie. drive port B with pipe B, or port C with pipe A.

For single channel PHY (CHV):

pipe C == CMN/PLL/REF CH0

port D == PCS/TX CH0

On BXT the entire PHY channel corresponds to the port. That means the PLL is also now associated with the port rather than the pipe, and so the clock needs to be routed to the
appropriate transcoder. Port A PLL is directly connected to transcoder EDP and port B/C PLLs can be routed to any transcoder A/B/C.

Note: DDI0 is digital port B, DD1 is digital port C, and DDI2 is digital port D (CHV) or port A (BXT).

Dual channel PHY (VLV/CHV/BXT) --------------------------------- | CH0 | CH1 | | CMN/PLL/REF | CMN/PLL/REF | |---------------|---------------| Display PHY | PCS01 |
PCS23 | PCS01 | PCS23 | |-------|-------|-------|-------| |TX0|TX1|TX2|TX3|TX0|TX1|TX2|TX3| --------------------------------- | DDI0 | DDI1 | DP/HDMI ports
---------------------------------

Single channel PHY (CHV/BXT) ----------------- | CH0 | | CMN/PLL/REF | |---------------| Display PHY | PCS01 | PCS23 | |-------|-------| |TX0|TX1|TX2|TX3|
----------------- | DDI2 | DP/HDMI port -----------------


CSR firmware support for DMC
----------------------------

Display Context Save and Restore (CSR) firmware support added from gen9 onwards to drive newly added DMC (Display microcontroller) in display engine to save and restore the state
of display engine when it enter into low-power state and comes back to normal.

Firmware loading status will be one of the below states: FW_UNINITIALIZED, FW_LOADED, FW_FAILED.

Once the firmware is written into the registers status will be moved from FW_UNINITIALIZED to FW_LOADED and for any erroneous condition status will be moved to FW_FAILED.


.. toctree::
    :maxdepth: 1

    API-intel-csr-load-program
    API-intel-csr-ucode-init
    API-intel-csr-ucode-fini

Video BIOS Table (VBT)
----------------------

The Video BIOS Table, or VBT, provides platform and board specific configuration information to the driver that is not discoverable or available through other means. The
configuration is mostly related to display hardware. The VBT is available via the ACPI OpRegion or, on older systems, in the PCI ROM.

The VBT consists of a VBT Header (defined as ``struct vbt_header``), a BDB Header (``struct bdb_header``), and a number of BIOS Data Blocks (BDB) that contain the actual
configuration information. The VBT Header, and thus the VBT, begins with “$VBT” signature. The VBT Header contains the offset of the BDB Header. The data blocks are concatenated
after the BDB Header. The data blocks have a 1-byte Block ID, 2-byte Block Size, and Block Size bytes of data. (Block 53, the MIPI Sequence Block is an exception.)

The driver parses the VBT during load. The relevant information is stored in driver private data for ease of use, and the actual VBT is not read after that.


.. toctree::
    :maxdepth: 1

    API-intel-bios-is-valid-vbt
    API-intel-bios-init
    API-struct-vbt-header
    API-struct-bdb-header

Memory Management and Command Submission
========================================

This sections covers all things related to the GEM implementation in the i915 driver.


Batchbuffer Parsing
-------------------

Motivation: Certain OpenGL features (e.g. transform feedback, performance monitoring) require userspace code to submit batches containing commands such as MI_LOAD_REGISTER_IMM
to access various registers. Unfortunately, some generations of the hardware will noop these commands in “unsecure” batches (which includes all userspace batches submitted via
i915) even though the commands may be safe and represent the intended programming model of the device.

The software command parser is similar in operation to the command parsing done in hardware for unsecure batches. However, the software parser allows some operations that would be
noop'd by hardware, if the parser determines the operation is safe, and submits the batch as “secure” to prevent hardware parsing.

Threats: At a high level, the hardware (and software) checks attempt to prevent granting userspace undue privileges. There are three categories of privilege.

First, commands which are explicitly defined as privileged or which should only be used by the kernel driver. The parser generally rejects such commands, though it may allow some
from the drm master process.

Second, commands which access registers. To support correct/enhanced userspace functionality, particularly certain OpenGL extensions, the parser provides a whitelist of registers
which userspace may safely access (for both normal and drm master processes).

Third, commands which access privileged memory (i.e. GGTT, HWS page, etc). The parser always rejects such commands.

The majority of the problematic commands fall in the MI_⋆ range, with only a few specific commands on each ring (e.g. PIPE_CONTROL and MI_FLUSH_DW).

Implementation: Each ring maintains tables of commands and registers which the parser uses in scanning batch buffers submitted to that ring.

Since the set of commands that the parser must check for is significantly smaller than the number of commands supported, the parser tables contain only those commands required by
the parser. This generally works because command opcode ranges have standard command length encodings. So for commands that the parser does not need to check, it can easily skip
them. This is implemented via a per-ring length decoding vfunc.

Unfortunately, there are a number of commands that do not follow the standard length encoding for their opcode range, primarily amongst the MI_⋆ commands. To handle this, the
parser provides a way to define explicit “skip” entries in the per-ring command tables.

Other command table entries map fairly directly to high level categories mentioned above: rejected, master-only, register whitelist. The parser implements a number of checks,
including the privileged memory checks, via a general bitmasking mechanism.


.. toctree::
    :maxdepth: 1

    API-i915-cmd-parser-init-ring
    API-i915-cmd-parser-fini-ring
    API-i915-needs-cmd-parser
    API-i915-parse-cmds
    API-i915-cmd-parser-get-version

Batchbuffer Pools
-----------------

In order to submit batch buffers as 'secure', the software command parser must ensure that a batch buffer cannot be modified after parsing. It does this by copying the user
provided batch buffer contents to a kernel owned buffer from which the hardware will actually execute, and by carefully managing the address space bindings for such buffers.

The batch pool framework provides a mechanism for the driver to manage a set of scratch buffers to use for this purpose. The framework can be extended to support other uses cases
should they arise.


.. toctree::
    :maxdepth: 1

    API-i915-gem-batch-pool-init
    API-i915-gem-batch-pool-fini
    API-i915-gem-batch-pool-get

Logical Rings, Logical Ring Contexts and Execlists
--------------------------------------------------

Motivation: GEN8 brings an expansion of the HW contexts: “Logical Ring Contexts”. These expanded contexts enable a number of new abilities, especially “Execlists” (also implemented
in this file).

One of the main differences with the legacy HW contexts is that logical ring contexts incorporate many more things to the context's state, like PDPs or ringbuffer control
registers:

The reason why PDPs are included in the context is straightforward: as PPGTTs (per-process GTTs) are actually per-context, having the PDPs contained there mean you don't need to do
a ppgtt->switch_mm yourself, instead, the GPU will do it for you on the context switch.

But, what about the ringbuffer control registers (head, tail, etc..)? shouldn't we just need a set of those per engine command streamer? This is where the name “Logical Rings”
starts to make sense: by virtualizing the rings, the engine cs shifts to a new “ring buffer” with every context switch. When you want to submit a workload to the GPU you: A) choose
your context, B) find its appropriate virtualized ring, C) write commands to it and then, finally, D) tell the GPU to switch to that context.

Instead of the legacy MI_SET_CONTEXT, the way you tell the GPU to switch to a contexts is via a context execution list, ergo “Execlists”.

LRC implementation: Regarding the creation of contexts, we have:

- One global default context. - One local default context for each opened fd. - One local extra context for each context create ioctl call.

Now that ringbuffers belong per-context (and not per-engine, like before) and that contexts are uniquely tied to a given engine (and not reusable, like before) we need:

- One ringbuffer per-engine inside each context. - One backing object per-engine inside each context.

The global default context starts its life with these new objects fully allocated and populated. The local default context for each opened fd is more complex, because we don't know
at creation time which engine is going to use them. To handle this, we have implemented a deferred creation of LR contexts:

The local context starts its life as a hollow or blank holder, that only gets populated for a given engine once we receive an execbuffer. If later on we receive another execbuffer
ioctl for the same context but a different engine, we allocate/populate a new ringbuffer and context backing object and so on.

Finally, regarding local contexts created using the ioctl call: as they are only allowed with the render ring, we can allocate & populate them right away (no need to defer
anything, at least for now).

Execlists implementation: Execlists are the new method by which, on gen8+ hardware, workloads are submitted for execution (as opposed to the legacy, ringbuffer-based, method). This
method works as follows:

When a request is committed, its commands (the BB start and any leading or trailing commands, like the seqno breadcrumbs) are placed in the ringbuffer for the appropriate context.
The tail pointer in the hardware context is not updated at this time, but instead, kept by the driver in the ringbuffer structure. A structure representing this request is added to
a request queue for the appropriate engine: this structure contains a copy of the context's tail after the request was written to the ring buffer and a pointer to the context
itself.

If the engine's request queue was empty before the request was added, the queue is processed immediately. Otherwise the queue will be processed during a context switch interrupt.
In any case, elements on the queue will get sent (in pairs) to the GPU's ExecLists Submit Port (ELSP, for short) with a globally unique 20-bits submission ID.

When execution of a request completes, the GPU updates the context status buffer with a context complete event and generates a context switch interrupt. During the interrupt
handling, the driver examines the events in the buffer: for each context complete event, if the announced ID matches that on the head of the request queue, then that request is
retired and removed from the queue.

After processing, if any requests were retired and the queue is not empty then a new execution list can be submitted. The two requests at the front of the queue are next to be
submitted but since a context may not occur twice in an execution list, if subsequent requests have the same ID as the first then the two requests must be combined. This is done
simply by discarding requests at the head of the queue until either only one requests is left (in which case we use a NULL second context) or the first two requests have unique
IDs.

By always executing the first two requests in the queue the driver ensures that the GPU is kept as busy as possible. In the case where a single context completes but a second
context is still executing, the request for this second context will be at the head of the queue when we remove the first one. This request will then be resubmitted along with a
new request for a different context, which will cause the hardware to continue executing the second request and queue the new request (the GPU detects the condition of a context
getting preempted with the same context and optimizes the context switch flow by not doing preemption, but just sampling the new tail pointer).


.. toctree::
    :maxdepth: 1

    API-intel-sanitize-enable-execlists
    API-intel-lr-context-descriptor-update
    API-intel-execlists-ctx-id
    API-intel-lrc-irq-handler
    API-intel-logical-ring-begin
    API-intel-execlists-submission
    API-gen8-init-indirectctx-bb
    API-gen8-init-perctx-bb
    API-intel-logical-ring-cleanup
    API-intel-logical-rings-init
    API-intel-lr-context-free
    API-intel-lr-context-size
    API-intel-lr-context-deferred-alloc

Global GTT views
----------------

Background and previous state

Historically objects could exists (be bound) in global GTT space only as singular instances with a view representing all of the object's backing pages in a linear fashion. This
view will be called a normal view.

To support multiple views of the same object, where the number of mapped pages is not equal to the backing store, or where the layout of the pages is not linear, concept of a GGTT
view was added.

One example of an alternative view is a stereo display driven by a single image. In this case we would have a framebuffer looking like this (2x2 pages):

12 34

Above would represent a normal GGTT view as normally mapped for GPU or CPU rendering. In contrast, fed to the display engine would be an alternative view which could look something
like this:

1212 3434

In this example both the size and layout of pages in the alternative view is different from the normal view.

Implementation and usage

GGTT views are implemented using VMAs and are distinguished via enum i915_ggtt_view_type and struct i915_ggtt_view.

A new flavour of core GEM functions which work with GGTT bound objects were added with the _ggtt_ infix, and sometimes with _view postfix to avoid renaming in large amounts of
code. They take the struct i915_ggtt_view parameter encapsulating all metadata required to implement a view.

As a helper for callers which are only interested in the normal view, globally const i915_ggtt_view_normal singleton instance exists. All old core GEM API functions, the ones
not taking the view parameter, are operating on, or with the normal GGTT view.

Code wanting to add or use a new GGTT view needs to:

1. Add a new enum with a suitable name. 2. Extend the metadata in the i915_ggtt_view structure if required. 3. Add support to ``i915_get_vma_pages``.

New views are required to build a scatter-gather table from within the i915_get_vma_pages function. This table is stored in the vma.ggtt_view and exists for the lifetime of an
VMA.

Core API is designed to have copy semantics which means that passed in struct i915_ggtt_view does not need to be persistent (left around after calling the core API functions).


.. toctree::
    :maxdepth: 1

    API-gen8-ppgtt-alloc-pagetabs
    API-gen8-ppgtt-alloc-page-directories
    API-gen8-ppgtt-alloc-page-dirpointers
    API-i915-vma-bind
    API-i915-ggtt-view-size

GTT Fences and Swizzling
------------------------


.. toctree::
    :maxdepth: 1

    API-i915-gem-object-put-fence
    API-i915-gem-object-get-fence
    API-i915-gem-object-pin-fence
    API-i915-gem-object-unpin-fence
    API-i915-gem-restore-fences
    API-i915-gem-detect-bit-6-swizzle
    API-i915-gem-object-do-bit-17-swizzle
    API-i915-gem-object-save-bit-17-swizzle

Global GTT Fence Handling
+++++++++++++++++++++++++

Important to avoid confusions: “fences” in the i915 driver are not execution fences used to track command completion but hardware detiler objects which wrap a given range of the
global GTT. Each platform has only a fairly limited set of these objects.

Fences are used to detile GTT memory mappings. They're also connected to the hardware frontbuffer render tracking and hence interact with frontbuffer compression. Furthermore on
older platforms fences are required for tiled objects used by the display engine. They can also be used by the render engine - they're required for blitter commands and are
optional for render commands. But on gen4+ both display (with the exception of fbc) and rendering have their own tiling state bits and don't need fences.

Also note that fences only support X and Y tiling and hence can't be used for the fancier new tiling formats like W, Ys and Yf.

Finally note that because fences are such a restricted resource they're dynamically associated with objects. Furthermore fence state is committed to the hardware lazily to avoid
unnecessary stalls on gen2/3. Therefore code must explicitly call ``i915_gem_object_get_fence`` to synchronize fencing status for cpu access. Also note that some code wants an
unfenced view, for those cases the fence can be removed forcefully with ``i915_gem_object_put_fence``.

Internally these functions will synchronize with userspace access by removing CPU ptes into GTT mmaps (not the GTT ptes themselves) as needed.


Hardware Tiling and Swizzling Details
+++++++++++++++++++++++++++++++++++++

The idea behind tiling is to increase cache hit rates by rearranging pixel data so that a group of pixel accesses are in the same cacheline. Performance improvement from doing this
on the back/depth buffer are on the order of 30%.

Intel architectures make this somewhat more complicated, though, by adjustments made to addressing of data when the memory is in interleaved mode (matched pairs of DIMMS) to
improve memory bandwidth. For interleaved memory, the CPU sends every sequential 64 bytes to an alternate memory channel so it can get the bandwidth from both.

The GPU also rearranges its accesses for increased bandwidth to interleaved memory, and it matches what the CPU does for non-tiled. However, when tiled it does it a little
differently, since one walks addresses not just in the X direction but also Y. So, along with alternating channels when bit 6 of the address flips, it also alternates when other
bits flip -- Bits 9 (every 512 bytes, an X tile scanline) and 10 (every two X tile scanlines) are common to both the 915 and 965-class hardware.

The CPU also sometimes XORs in higher bits as well, to improve bandwidth doing strided access like we do so frequently in graphics. This is called “Channel XOR Randomization” in
the MCH documentation. The result is that the CPU is XORing in either bit 11 or bit 17 to bit 6 of its address decode.

All of this bit 6 XORing has an effect on our memory management, as we need to make sure that the 3d driver can correctly address object contents.

If we don't have interleaved memory, all tiling is safe and no swizzling is required.

When bit 17 is XORed in, we simply refuse to tile at all. Bit 17 is not just a page offset, so as we page an object out and back in, individual pages in it will have different bit
17 addresses, resulting in each 64 bytes being swapped with its neighbor!

Otherwise, if interleaved, we have to tell the 3d driver what the address swizzling it needs to do is, since it's writing with the CPU to the pages (bit 6 and potentially bit 11
XORed in), and the GPU is reading from the pages (bit 6, 9, and 10 XORed in), resulting in a cumulative bit swizzling required by the CPU of XORing in bit 6, 9, 10, and potentially
11, in order to match what the GPU expects.


Object Tiling IOCTLs
--------------------


.. toctree::
    :maxdepth: 1

    API-i915-gem-set-tiling
    API-i915-gem-get-tiling
``i915_gem_set_tiling`` and ``i915_gem_get_tiling`` is the userspace interface to declare fence register requirements.

In principle GEM doesn't care at all about the internal data layout of an object, and hence it also doesn't care about tiling or swizzling. There's two exceptions:

- For X and Y tiling the hardware provides detilers for CPU access, so called fences. Since there's only a limited amount of them the kernel must manage these, and therefore
userspace must tell the kernel the object tiling if it wants to use fences for detiling. - On gen3 and gen4 platforms have a swizzling pattern for tiled objects which depends upon
the physical page frame number. When swapping such objects the page frame number might change and the kernel must be able to fix this up and hence now the tiling. Note that on a
subset of platforms with asymmetric memory channel population the swizzling pattern changes in an unknown way, and for those the kernel simply forbids swapping completely.

Since neither of this applies for new tiling layouts on modern platforms like W, Ys and Yf tiling GEM only allows object tiling to be set to X or Y tiled. Anything else can be
handled in userspace entirely without the kernel's invovlement.


Buffer Object Eviction
----------------------

This section documents the interface functions for evicting buffer objects to make space available in the virtual gpu address spaces. Note that this is mostly orthogonal to
shrinking buffer objects caches, which has the goal to make main memory (shared with the gpu through the unified memory architecture) available.


.. toctree::
    :maxdepth: 1

    API-i915-gem-evict-something
    API-i915-gem-evict-vm

Buffer Object Memory Shrinking
------------------------------

This section documents the interface function for shrinking memory usage of buffer object caches. Shrinking is used to make main memory available. Note that this is mostly
orthogonal to evicting buffer objects, which has the goal to make space in gpu virtual address spaces.


.. toctree::
    :maxdepth: 1

    API-i915-gem-shrink
    API-i915-gem-shrink-all
    API-i915-gem-shrinker-init
    API-i915-gem-shrinker-cleanup

GuC
===


GuC-specific firmware loader
----------------------------

intel_guc: Top level structure of guc. It handles firmware loading and manages client pool and doorbells. intel_guc owns a i915_guc_client to replace the legacy ExecList
submission.

Firmware versioning: The firmware build process will generate a version header file with major and minor version defined. The versions are built into CSS header of firmware. i915
kernel driver set the minimal firmware version required per platform. The firmware installation package will install (symbolic link) proper version of firmware.

GuC address space: GuC does not allow any gfx GGTT address that falls into range [0, WOPCM_TOP), which is reserved for Boot ROM, SRAM and WOPCM. Currently this top address is
512K. In order to exclude 0-512K address space from GGTT, all gfx objects used by GuC is pinned with PIN_OFFSET_BIAS along with size of WOPCM.

Firmware log: Firmware log is enabled by setting i915.guc_log_level to non-negative level. Log data is printed out via reading debugfs i915_guc_log_dump. Reading from
i915_guc_load_status will print out firmware loading status and scratch registers value.


.. toctree::
    :maxdepth: 1

    API-intel-guc-ucode-load
    API-intel-guc-ucode-init
    API-intel-guc-ucode-fini

GuC-based command submission
----------------------------

i915_guc_client: We use the term client to avoid confusion with contexts. A i915_guc_client is equivalent to GuC object guc_context_desc. This context descriptor is allocated
from a pool of 1024 entries. Kernel driver will allocate doorbell and workqueue for it. Also the process descriptor (guc_process_desc), which is mapped to client space. So the
client can write Work Item then ring the doorbell.

To simplify the implementation, we allocate one gem object that contains all pages for doorbell, process descriptor and workqueue.

The Scratch registers: There are 16 MMIO-based registers start from 0xC180. The kernel driver writes a value to the action register (SOFT_SCRATCH_0) along with any data. It then
triggers an interrupt on the GuC via another register write (0xC4C8). Firmware writes a success/fail code back to the action register after processes the request. The kernel driver
polls waiting for this update and then proceeds. See ``host2guc_action``

Doorbells: Doorbells are interrupts to uKernel. A doorbell is a single cache line (QW) mapped into process space.

Work Items: There are several types of work items that the host may place into a workqueue, each with its own requirements and limitations. Currently only WQ_TYPE_INORDER is
needed to support legacy submission via GuC, which represents in-order queue. The kernel driver packs ring tail pointer and an ELSP context descriptor dword into Work Item. See
``guc_add_workqueue_item``


.. toctree::
    :maxdepth: 1

    API-i915-guc-submit
    API-gem-allocate-guc-obj
    API-gem-release-guc-obj
    API-guc-client-alloc
    API-intel-guc-suspend
    API-intel-guc-resume

GuC Firmware Layout
-------------------

The GuC firmware layout looks like this:

+-------------------------------+ | guc_css_header | | contains major/minor version | +-------------------------------+ | uCode | +-------------------------------+ | RSA
signature | +-------------------------------+ | modulus key | +-------------------------------+ | exponent val | +-------------------------------+

The firmware may or may not have modulus key and exponent data. The header, uCode and RSA signature are must-have components that will be used by driver. Length of each components,
which is all in dwords, can be found in header. In the case that modulus and exponent are not present in fw, a.k.a truncated image, the length value still appears in header.

Driver will do some basic fw size validation based on the following rules:

1. Header, uCode and RSA are must-have components. 2. All firmware components, if they present, are in the sequence illustrated in the layout table above. 3. Length info of each
component can be found in header, in dwords. 4. Modulus and exponent key are not required by driver. They may not appear in fw. So driver will load a truncated firmware in this
case.


Tracing
=======

This sections covers all things related to the tracepoints implemented in the i915 driver.


i915_ppgtt_create and i915_ppgtt_release
----------------------------------------

With full ppgtt enabled each process using drm will allocate at least one translation table. With these traces it is possible to keep track of the allocation and of the lifetime of
the tables; this can be used during testing/debug to verify that we are not leaking ppgtts. These traces identify the ppgtt through the vm pointer, which is also printed by the
i915_vma_bind and i915_vma_unbind tracepoints.


i915_context_create and i915_context_free
-----------------------------------------

These tracepoints are used to track creation and deletion of contexts. If full ppgtt is enabled, they also print the address of the vm assigned to the context.


switch_mm
---------

This tracepoint allows tracking of the mm switch, which is an important point in the lifetime of the vm in the legacy submission path. This tracepoint is called only if full ppgtt
is enabled.
