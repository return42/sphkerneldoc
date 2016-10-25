.. -*- coding: utf-8; mode: rst -*-

.. _CommonBackEndReq:

*************************
Kernel Debugger Internals
*************************


.. _kgdbArchitecture:

Architecture Specifics
======================

The kernel debugger is organized into a number of components:

1. The debug core

   The debug core is found in kernel/debugger/debug_core.c. It
   contains:

   -  A generic OS exception handler which includes sync'ing the
      processors into a stopped state on an multi-CPU system.

   -  The API to talk to the kgdb I/O drivers

   -  The API to make calls to the arch-specific kgdb implementation

   -  The logic to perform safe memory reads and writes to memory while
      using the debugger

   -  A full implementation for software breakpoints unless overridden
      by the arch

   -  The API to invoke either the kdb or kgdb frontend to the debug
      core.

   -  The structures and callback API for atomic kernel mode setting.

      NOTE: kgdboc is where the kms callbacks are invoked.

2. kgdb arch-specific implementation

   This implementation is generally found in arch/*/kernel/kgdb.c. As an
   example, arch/x86/kernel/kgdb.c contains the specifics to implement
   HW breakpoint as well as the initialization to dynamically register
   and unregister for the trap handlers on this architecture. The
   arch-specific portion implements:

   -  contains an arch-specific trap catcher which invokes
      kgdb_handle_exception() to start kgdb about doing its work

   -  translation to and from gdb specific packet format to pt_regs

   -  Registration and unregistration of architecture specific trap
      hooks

   -  Any special exception handling and cleanup

   -  NMI exception handling and cleanup

   -  (optional) HW breakpoints

3. gdbstub frontend (aka kgdb)

   The gdbstub is located in kernel/debug/gdbstub.c. It contains:

   -  All the logic to implement the gdb serial protocol

4. kdb frontend

   The kdb debugger shell is broken down into a number of components.
   The kdb core is located in kernel/debug/kdb. There are a number of
   helper functions in some of the other kernel components to make it
   possible for kdb to examine and report information about the kernel
   without taking locks that could cause a kernel deadlock. The kdb core
   contains implements the following functionality.

   -  A simple shell

   -  The kdb core command set

   -  A registration API to register additional kdb shell commands.

      -  A good example of a self-contained kdb module is the "ftdump"
         command for dumping the ftrace buffer. See:
         kernel/trace/trace_kdb.c

      -  For an example of how to dynamically register a new kdb command
         you can build the kdb_hello.ko kernel module from
         samples/kdb/kdb_hello.c. To build this example you can set
         CONFIG_SAMPLES=y and CONFIG_SAMPLE_KDB=m in your kernel
         config. Later run "modprobe kdb_hello" and the next time you
         enter the kdb shell, you can run the "hello" command.

   -  The implementation for kdb_printf() which emits messages directly
      to I/O drivers, bypassing the kernel log.

   -  SW / HW breakpoint management for the kdb shell

5. kgdb I/O driver

   Each kgdb I/O driver has to provide an implementation for the
   following:

   -  configuration via built-in or module

   -  dynamic configuration and kgdb hook registration calls

   -  read and write character interface

   -  A cleanup handler for unconfiguring from the kgdb core

   -  (optional) Early debug methodology

   Any given kgdb I/O driver has to operate very closely with the
   hardware and must do it in such a way that does not enable interrupts
   or change other parts of the system context without completely
   restoring them. The kgdb core will repeatedly "poll" a kgdb I/O
   driver for characters when it needs input. The I/O driver is expected
   to return immediately if there is no data available. Doing so allows
   for the future possibility to touch watchdog hardware in such a way
   as to have a target system not reset when these are enabled.

If you are intent on adding kgdb architecture specific support for a new
architecture, the architecture should define ``HAVE_ARCH_KGDB`` in the
architecture specific Kconfig file. This will enable kgdb for the
architecture, and at that point you must create an architecture specific
kgdb implementation.

There are a few flags which must be set on every architecture in their
<asm/kgdb.h> file. These are:

-  NUMREGBYTES: The size in bytes of all of the registers, so that we
   can ensure they will all fit into a packet.

-  BUFMAX: The size in bytes of the buffer GDB will read into. This must
   be larger than NUMREGBYTES.

-  CACHE_FLUSH_IS_SAFE: Set to 1 if it is always safe to call
   flush_cache_range or flush_icache_range. On some architectures,
   these functions may not be safe to call on SMP since we keep other
   CPUs in a holding pattern.

There are also the following functions for the common backend, found in
kernel/kgdb.c, that must be supplied by the architecture-specific
backend unless marked as (optional), in which case a default function
maybe used if the architecture does not need to provide a specific
implementation.


.. kernel-doc:: include/linux/kgdb.h
    :man-sect: 9
    :internal:


.. _kgdbocDesign:

kgdboc internals
================


kgdboc and uarts
----------------

The kgdboc driver is actually a very thin driver that relies on the
underlying low level to the hardware driver having "polling hooks" to
which the tty driver is attached. In the initial implementation of
kgdboc the serial_core was changed to expose a low level UART hook for
doing polled mode reading and writing of a single character while in an
atomic context. When kgdb makes an I/O request to the debugger, kgdboc
invokes a callback in the serial core which in turn uses the callback in
the UART driver.

When using kgdboc with a UART, the UART driver must implement two
callbacks in the ``struct uart_ops``. Example from drivers/8250.c:


.. code-block:: c

    #ifdef CONFIG_CONSOLE_POLL
        .poll_get_char = serial8250_get_poll_char,
        .poll_put_char = serial8250_put_poll_char,
    #endif

Any implementation specifics around creating a polling driver use the
``#ifdef CONFIG_CONSOLE_POLL``, as shown above. Keep in mind that
polling hooks have to be implemented in such a way that they can be
called from an atomic context and have to restore the state of the UART
chip on return such that the system can return to normal when the
debugger detaches. You need to be very careful with any kind of lock you
consider, because failing here is most likely going to mean pressing the
reset button.


.. _kgdbocKbd:

kgdboc and keyboards
--------------------

The kgdboc driver contains logic to configure communications with an
attached keyboard. The keyboard infrastructure is only compiled into the
kernel when CONFIG_KDB_KEYBOARD=y is set in the kernel configuration.

The core polled keyboard driver driver for PS/2 type keyboards is in
drivers/char/kdb_keyboard.c. This driver is hooked into the debug core
when kgdboc populates the callback in the array called
``kdb_poll_funcs[]``. The kdb_get_kbd_char() is the top-level
function which polls hardware for single character input.


.. _kgdbocKms:

kgdboc and kms
--------------

The kgdboc driver contains logic to request the graphics display to
switch to a text context when you are using "kgdboc=kms,kbd", provided
that you have a video driver which has a frame buffer console and atomic
kernel mode setting support.

Every time the kernel debugger is entered it calls
kgdboc_pre_exp_handler() which in turn calls con_debug_enter() in
the virtual console layer. On resuming kernel execution, the kernel
debugger calls kgdboc_post_exp_handler() which in turn calls
con_debug_leave().

Any video driver that wants to be compatible with the kernel debugger
and the atomic kms callbacks must implement the mode_set_base_atomic,
fb_debug_enter and fb_debug_leave operations. For the
fb_debug_enter and fb_debug_leave the option exists to use the
generic drm fb helper functions or implement something custom for the
hardware. The following example shows the initialization of the
.mode_set_base_atomic operation in
drivers/gpu/drm/i915/intel_display.c:


.. code-block:: c

    static const struct drm_crtc_helper_funcs intel_helper_funcs = {
    [...]
            .mode_set_base_atomic = intel_pipe_set_base_atomic,
    [...]
    };

Here is an example of how the i915 driver initializes the
fb_debug_enter and fb_debug_leave functions to use the generic drm
helpers in drivers/gpu/drm/i915/intel_fb.c:


.. code-block:: c

    static struct fb_ops intelfb_ops = {
    [...]
           .fb_debug_enter = drm_fb_helper_debug_enter,
           .fb_debug_leave = drm_fb_helper_debug_leave,
    [...]
    };




.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/dbxml2rst). The origin XML comes
.. from the linux kernel:
..
..   http://git.kernel.org/cgit/linux/kernel/git/torvalds/linux.git
.. ------------------------------------------------------------------------------
