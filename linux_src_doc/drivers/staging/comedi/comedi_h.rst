.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/comedi/comedi.h

.. _`comedi_subdevice_type`:

enum comedi_subdevice_type
==========================

.. c:type:: enum comedi_subdevice_type

    COMEDI subdevice types

.. _`comedi_subdevice_type.definition`:

Definition
----------

.. code-block:: c

    enum comedi_subdevice_type {
        COMEDI_SUBD_UNUSED,
        COMEDI_SUBD_AI,
        COMEDI_SUBD_AO,
        COMEDI_SUBD_DI,
        COMEDI_SUBD_DO,
        COMEDI_SUBD_DIO,
        COMEDI_SUBD_COUNTER,
        COMEDI_SUBD_TIMER,
        COMEDI_SUBD_MEMORY,
        COMEDI_SUBD_CALIB,
        COMEDI_SUBD_PROC,
        COMEDI_SUBD_SERIAL,
        COMEDI_SUBD_PWM
    };

.. _`comedi_subdevice_type.constants`:

Constants
---------

COMEDI_SUBD_UNUSED
    Unused subdevice.

COMEDI_SUBD_AI
    Analog input.

COMEDI_SUBD_AO
    Analog output.

COMEDI_SUBD_DI
    Digital input.

COMEDI_SUBD_DO
    Digital output.

COMEDI_SUBD_DIO
    Digital input/output.

COMEDI_SUBD_COUNTER
    Counter.

COMEDI_SUBD_TIMER
    Timer.

COMEDI_SUBD_MEMORY
    Memory, EEPROM, DPRAM.

COMEDI_SUBD_CALIB
    Calibration DACs.

COMEDI_SUBD_PROC
    Processor, DSP.

COMEDI_SUBD_SERIAL
    Serial I/O.

COMEDI_SUBD_PWM
    Pulse-Width Modulation output.

.. _`comedi_io_direction`:

enum comedi_io_direction
========================

.. c:type:: enum comedi_io_direction

    COMEDI I/O directions

.. _`comedi_io_direction.definition`:

Definition
----------

.. code-block:: c

    enum comedi_io_direction {
        COMEDI_INPUT,
        COMEDI_OUTPUT,
        COMEDI_OPENDRAIN
    };

.. _`comedi_io_direction.constants`:

Constants
---------

COMEDI_INPUT
    Input.

COMEDI_OUTPUT
    Output.

COMEDI_OPENDRAIN
    Open-drain (or open-collector) output.

.. _`comedi_io_direction.description`:

Description
-----------

These are used by the \ ``INSN_CONFIG_DIO_QUERY``\  configuration instruction to
report a direction.  They may also be used in other places where a direction
needs to be specified.

.. _`configuration_ids`:

enum configuration_ids
======================

.. c:type:: enum configuration_ids

    COMEDI configuration instruction codes

.. _`configuration_ids.definition`:

Definition
----------

.. code-block:: c

    enum configuration_ids {
        INSN_CONFIG_DIO_INPUT,
        INSN_CONFIG_DIO_OUTPUT,
        INSN_CONFIG_DIO_OPENDRAIN,
        INSN_CONFIG_ANALOG_TRIG,
        INSN_CONFIG_ALT_SOURCE,
        INSN_CONFIG_DIGITAL_TRIG,
        INSN_CONFIG_BLOCK_SIZE,
        INSN_CONFIG_TIMER_1,
        INSN_CONFIG_FILTER,
        INSN_CONFIG_CHANGE_NOTIFY,
        INSN_CONFIG_SERIAL_CLOCK,
        INSN_CONFIG_BIDIRECTIONAL_DATA,
        INSN_CONFIG_DIO_QUERY,
        INSN_CONFIG_PWM_OUTPUT,
        INSN_CONFIG_GET_PWM_OUTPUT,
        INSN_CONFIG_ARM,
        INSN_CONFIG_DISARM,
        INSN_CONFIG_GET_COUNTER_STATUS,
        INSN_CONFIG_RESET,
        INSN_CONFIG_GPCT_SINGLE_PULSE_GENERATOR,
        INSN_CONFIG_GPCT_PULSE_TRAIN_GENERATOR,
        INSN_CONFIG_GPCT_QUADRATURE_ENCODER,
        INSN_CONFIG_SET_GATE_SRC,
        INSN_CONFIG_GET_GATE_SRC,
        INSN_CONFIG_SET_CLOCK_SRC,
        INSN_CONFIG_GET_CLOCK_SRC,
        INSN_CONFIG_SET_OTHER_SRC,
        INSN_CONFIG_GET_HARDWARE_BUFFER_SIZE,
        INSN_CONFIG_SET_COUNTER_MODE,
        INSN_CONFIG_8254_SET_MODE,
        INSN_CONFIG_8254_READ_STATUS,
        INSN_CONFIG_SET_ROUTING,
        INSN_CONFIG_GET_ROUTING,
        INSN_CONFIG_PWM_SET_PERIOD,
        INSN_CONFIG_PWM_GET_PERIOD,
        INSN_CONFIG_GET_PWM_STATUS,
        INSN_CONFIG_PWM_SET_H_BRIDGE,
        INSN_CONFIG_PWM_GET_H_BRIDGE
    };

.. _`configuration_ids.constants`:

Constants
---------

INSN_CONFIG_DIO_INPUT
    Configure digital I/O as input.

INSN_CONFIG_DIO_OUTPUT
    Configure digital I/O as output.

INSN_CONFIG_DIO_OPENDRAIN
    Configure digital I/O as open-drain (or open
    collector) output.

INSN_CONFIG_ANALOG_TRIG
    Configure analog trigger.

INSN_CONFIG_ALT_SOURCE
    Configure alternate input source.

INSN_CONFIG_DIGITAL_TRIG
    Configure digital trigger.

INSN_CONFIG_BLOCK_SIZE
    Configure block size for DMA transfers.

INSN_CONFIG_TIMER_1
    Configure divisor for external clock.

INSN_CONFIG_FILTER
    Configure a filter.

INSN_CONFIG_CHANGE_NOTIFY
    Configure change notification for digital
    inputs.  (New drivers should use
    \ ``INSN_CONFIG_DIGITAL_TRIG``\  instead.)

INSN_CONFIG_SERIAL_CLOCK
    Configure clock for serial I/O.

INSN_CONFIG_BIDIRECTIONAL_DATA
    Send and receive byte over serial I/O.

INSN_CONFIG_DIO_QUERY
    Query direction of digital I/O channel.

INSN_CONFIG_PWM_OUTPUT
    Configure pulse-width modulator output.

INSN_CONFIG_GET_PWM_OUTPUT
    Get pulse-width modulator output configuration.

INSN_CONFIG_ARM
    Arm a subdevice or channel.

INSN_CONFIG_DISARM
    Disarm a subdevice or channel.

INSN_CONFIG_GET_COUNTER_STATUS
    Get counter status.

INSN_CONFIG_RESET
    Reset a subdevice or channel.

INSN_CONFIG_GPCT_SINGLE_PULSE_GENERATOR
    Configure counter/timer as
    single pulse generator.

INSN_CONFIG_GPCT_PULSE_TRAIN_GENERATOR
    Configure counter/timer as
    pulse train generator.

INSN_CONFIG_GPCT_QUADRATURE_ENCODER
    Configure counter as a quadrature
    encoder.

INSN_CONFIG_SET_GATE_SRC
    Set counter/timer gate source.

INSN_CONFIG_GET_GATE_SRC
    Get counter/timer gate source.

INSN_CONFIG_SET_CLOCK_SRC
    Set counter/timer master clock source.

INSN_CONFIG_GET_CLOCK_SRC
    Get counter/timer master clock source.

INSN_CONFIG_SET_OTHER_SRC
    Set counter/timer "other" source.

INSN_CONFIG_GET_HARDWARE_BUFFER_SIZE
    Get size (in bytes) of subdevice's
    on-board FIFOs used during streaming
    input/output.

INSN_CONFIG_SET_COUNTER_MODE
    Set counter/timer mode.

INSN_CONFIG_8254_SET_MODE
    (Deprecated) Same as
    \ ``INSN_CONFIG_SET_COUNTER_MODE``\ .

INSN_CONFIG_8254_READ_STATUS
    Read status of 8254 counter channel.

INSN_CONFIG_SET_ROUTING
    Set routing for a channel.

INSN_CONFIG_GET_ROUTING
    Get routing for a channel.

INSN_CONFIG_PWM_SET_PERIOD
    Set PWM period in nanoseconds.

INSN_CONFIG_PWM_GET_PERIOD
    Get PWM period in nanoseconds.

INSN_CONFIG_GET_PWM_STATUS
    Get PWM status.

INSN_CONFIG_PWM_SET_H_BRIDGE
    Set PWM H bridge duty cycle and polarity for
    a relay simultaneously.

INSN_CONFIG_PWM_GET_H_BRIDGE
    Get PWM H bridge duty cycle and polarity.

.. _`comedi_digital_trig_op`:

enum comedi_digital_trig_op
===========================

.. c:type:: enum comedi_digital_trig_op

    operations for configuring a digital trigger

.. _`comedi_digital_trig_op.definition`:

Definition
----------

.. code-block:: c

    enum comedi_digital_trig_op {
        COMEDI_DIGITAL_TRIG_DISABLE,
        COMEDI_DIGITAL_TRIG_ENABLE_EDGES,
        COMEDI_DIGITAL_TRIG_ENABLE_LEVELS
    };

.. _`comedi_digital_trig_op.constants`:

Constants
---------

COMEDI_DIGITAL_TRIG_DISABLE
    Return digital trigger to its default,
    inactive, unconfigured state.

COMEDI_DIGITAL_TRIG_ENABLE_EDGES
    Set rising and/or falling edge inputs
    that each can fire the trigger.

COMEDI_DIGITAL_TRIG_ENABLE_LEVELS
    Set a combination of high and/or low
    level inputs that can fire the trigger.

.. _`comedi_digital_trig_op.description`:

Description
-----------

These are used with the \ ``INSN_CONFIG_DIGITAL_TRIG``\  configuration instruction.
The data for the configuration instruction is as follows...

data[%0] = \ ``INSN_CONFIG_DIGITAL_TRIG``\ 

data[%1] = trigger ID

data[%2] = configuration operation

data[%3] = configuration parameter 1

data[%4] = configuration parameter 2

data[%5] = configuration parameter 3

The trigger ID (data[%1]) is used to differentiate multiple digital triggers
belonging to the same subdevice.  The configuration operation (data[%2]) is
one of the enum comedi_digital_trig_op values.  The configuration
parameters (data[%3], data[%4], and data[%5]) depend on the operation; they
are not used with \ ``COMEDI_DIGITAL_TRIG_DISABLE``\ .

For \ ``COMEDI_DIGITAL_TRIG_ENABLE_EDGES``\  and \ ``COMEDI_DIGITAL_TRIG_ENABLE_LEVELS``\ ,
configuration parameter 1 (data[%3]) contains a "left-shift" value that
specifies the input corresponding to bit 0 of configuration parameters 2
and 3.  This is useful if the trigger has more than 32 inputs.

For \ ``COMEDI_DIGITAL_TRIG_ENABLE_EDGES``\ , configuration parameter 2 (data[%4])
specifies which of up to 32 inputs have rising-edge sensitivity, and
configuration parameter 3 (data[%5]) specifies which of up to 32 inputs
have falling-edge sensitivity that can fire the trigger.

For \ ``COMEDI_DIGITAL_TRIG_ENABLE_LEVELS``\ , configuration parameter 2 (data[%4])
specifies which of up to 32 inputs must be at a high level, and
configuration parameter 3 (data[%5]) specifies which of up to 32 inputs
must be at a low level for the trigger to fire.

Some sequences of \ ``INSN_CONFIG_DIGITAL_TRIG``\  instructions may have a (partly)
accumulative effect, depending on the low-level driver.  This is useful
when setting up a trigger that has more than 32 inputs, or has a combination
of edge- and level-triggered inputs.

.. _`comedi_support_level`:

enum comedi_support_level
=========================

.. c:type:: enum comedi_support_level

    support level for a COMEDI feature

.. _`comedi_support_level.definition`:

Definition
----------

.. code-block:: c

    enum comedi_support_level {
        COMEDI_UNKNOWN_SUPPORT,
        COMEDI_SUPPORTED,
        COMEDI_UNSUPPORTED
    };

.. _`comedi_support_level.constants`:

Constants
---------

COMEDI_UNKNOWN_SUPPORT
    Unspecified support for feature.

COMEDI_SUPPORTED
    Feature is supported.

COMEDI_UNSUPPORTED
    Feature is unsupported.

.. _`comedi_counter_status_flags`:

enum comedi_counter_status_flags
================================

.. c:type:: enum comedi_counter_status_flags

    counter status bits

.. _`comedi_counter_status_flags.definition`:

Definition
----------

.. code-block:: c

    enum comedi_counter_status_flags {
        COMEDI_COUNTER_ARMED,
        COMEDI_COUNTER_COUNTING,
        COMEDI_COUNTER_TERMINAL_COUNT
    };

.. _`comedi_counter_status_flags.constants`:

Constants
---------

COMEDI_COUNTER_ARMED
    Counter is armed.

COMEDI_COUNTER_COUNTING
    Counter is counting.

COMEDI_COUNTER_TERMINAL_COUNT
    Counter reached terminal count.

.. _`comedi_counter_status_flags.description`:

Description
-----------

These bitwise values are used by the \ ``INSN_CONFIG_GET_COUNTER_STATUS``\ 
configuration instruction to report the status of a counter.

.. _`comedi_insn`:

struct comedi_insn
==================

.. c:type:: struct comedi_insn

    COMEDI instruction

.. _`comedi_insn.definition`:

Definition
----------

.. code-block:: c

    struct comedi_insn {
        unsigned int insn;
        unsigned int n;
        unsigned int __user *data;
        unsigned int subdev;
        unsigned int chanspec;
        unsigned int unused[3];
    }

.. _`comedi_insn.members`:

Members
-------

insn
    COMEDI instruction type (%INSN_xxx).

n
    Length of \ ``data``\ [].

data
    Pointer to data array operated on by the instruction.

subdev
    Subdevice index.

chanspec
    A packed "chanspec" value consisting of channel number,
    analog range index, analog reference type, and flags.

unused
    Reserved for future use.

.. _`comedi_insn.description`:

Description
-----------

This is used with the \ ``COMEDI_INSN``\  ioctl, and indirectly with the
\ ``COMEDI_INSNLIST``\  ioctl.

.. _`comedi_insnlist`:

struct comedi_insnlist
======================

.. c:type:: struct comedi_insnlist

    list of COMEDI instructions

.. _`comedi_insnlist.definition`:

Definition
----------

.. code-block:: c

    struct comedi_insnlist {
        unsigned int n_insns;
        struct comedi_insn __user *insns;
    }

.. _`comedi_insnlist.members`:

Members
-------

n_insns
    Number of COMEDI instructions.

insns
    Pointer to array COMEDI instructions.

.. _`comedi_insnlist.description`:

Description
-----------

This is used with the \ ``COMEDI_INSNLIST``\  ioctl.

.. _`comedi_cmd`:

struct comedi_cmd
=================

.. c:type:: struct comedi_cmd

    COMEDI asynchronous acquisition command details

.. _`comedi_cmd.definition`:

Definition
----------

.. code-block:: c

    struct comedi_cmd {
        unsigned int subdev;
        unsigned int flags;
        unsigned int start_src;
        unsigned int start_arg;
        unsigned int scan_begin_src;
        unsigned int scan_begin_arg;
        unsigned int convert_src;
        unsigned int convert_arg;
        unsigned int scan_end_src;
        unsigned int scan_end_arg;
        unsigned int stop_src;
        unsigned int stop_arg;
        unsigned int *chanlist;
        unsigned int chanlist_len;
        short __user *data;
        unsigned int data_len;
    }

.. _`comedi_cmd.members`:

Members
-------

subdev
    Subdevice index.

flags
    Command flags (%CMDF_xxx).

start_src
    "Start acquisition" trigger source (%TRIG_xxx).

start_arg
    "Start acquisition" trigger argument.

scan_begin_src
    "Scan begin" trigger source.

scan_begin_arg
    "Scan begin" trigger argument.

convert_src
    "Convert" trigger source.

convert_arg
    "Convert" trigger argument.

scan_end_src
    "Scan end" trigger source.

scan_end_arg
    "Scan end" trigger argument.

stop_src
    "Stop acquisition" trigger source.

stop_arg
    "Stop acquisition" trigger argument.

chanlist
    Pointer to array of "chanspec" values, containing a
    sequence of channel numbers packed with analog range
    index, etc.

chanlist_len
    Number of channels in sequence.

data
    Pointer to miscellaneous set-up data (not used).

data_len
    Length of miscellaneous set-up data.

.. _`comedi_cmd.description`:

Description
-----------

This is used with the \ ``COMEDI_CMD``\  or \ ``COMEDI_CMDTEST``\  ioctl to set-up
or validate an asynchronous acquisition command.  The ioctl may modify
the \ :c:type:`struct comedi_cmd <comedi_cmd>`\  and copy it back to the caller.

Optional command \ ``flags``\  values that can be ORed together...

\ ``CMDF_BOGUS``\  - makes \ ``COMEDI_CMD``\  ioctl return error \ ``EAGAIN``\  instead of
starting the command.

\ ``CMDF_PRIORITY``\  - requests "hard real-time" processing (which is not
supported in this version of COMEDI).

\ ``CMDF_WAKE_EOS``\  - requests the command makes data available for reading
after every "scan" period.

\ ``CMDF_WRITE``\  - marks the command as being in the "write" (to device)
direction.  This does not need to be specified by the caller unless the
subdevice supports commands in either direction.

\ ``CMDF_RAWDATA``\  - prevents the command from "munging" the data between the
COMEDI sample format and the raw hardware sample format.

\ ``CMDF_ROUND_NEAREST``\  - requests timing periods to be rounded to nearest
supported values.

\ ``CMDF_ROUND_DOWN``\  - requests timing periods to be rounded down to supported
values (frequencies rounded up).

\ ``CMDF_ROUND_UP``\  - requests timing periods to be rounded up to supported
values (frequencies rounded down).

Trigger source values for \ ``start_src``\ , \ ``scan_begin_src``\ , \ ``convert_src``\ ,
\ ``scan_end_src``\ , and \ ``stop_src...``\ 

\ ``TRIG_ANY``\  - "all ones" value used to test which trigger sources are
supported.

\ ``TRIG_INVALID``\  - "all zeroes" value used to indicate that all requested
trigger sources are invalid.

\ ``TRIG_NONE``\  - never trigger (often used as a \ ``stop_src``\  value).

\ ``TRIG_NOW``\  - trigger after '_arg' nanoseconds.

\ ``TRIG_FOLLOW``\  - trigger follows another event.

\ ``TRIG_TIMER``\  - trigger every '_arg' nanoseconds.

\ ``TRIG_COUNT``\  - trigger when count '_arg' is reached.

\ ``TRIG_EXT``\  - trigger on external signal specified by '_arg'.

\ ``TRIG_INT``\  - trigger on internal, software trigger specified by '_arg'.

\ ``TRIG_OTHER``\  - trigger on other, driver-defined signal specified by '_arg'.

.. _`comedi_chaninfo`:

struct comedi_chaninfo
======================

.. c:type:: struct comedi_chaninfo

    used to retrieve per-channel information

.. _`comedi_chaninfo.definition`:

Definition
----------

.. code-block:: c

    struct comedi_chaninfo {
        unsigned int subdev;
        unsigned int __user *maxdata_list;
        unsigned int __user *flaglist;
        unsigned int __user *rangelist;
        unsigned int unused[4];
    }

.. _`comedi_chaninfo.members`:

Members
-------

subdev
    Subdevice index.

maxdata_list
    Optional pointer to per-channel maximum data values.

flaglist
    Optional pointer to per-channel flags.

rangelist
    Optional pointer to per-channel range types.

unused
    Reserved for future use.

.. _`comedi_chaninfo.description`:

Description
-----------

This is used with the \ ``COMEDI_CHANINFO``\  ioctl to get per-channel information
for the subdevice.  Use of this requires knowledge of the number of channels
and subdevice flags obtained using the \ ``COMEDI_SUBDINFO``\  ioctl.

The \ ``maxdata_list``\  member must be \ ``NULL``\  unless the \ ``SDF_MAXDATA``\  subdevice
flag is set.  The \ ``flaglist``\  member must be \ ``NULL``\  unless the \ ``SDF_FLAGS``\ 
subdevice flag is set.  The \ ``rangelist``\  member must be \ ``NULL``\  unless the
\ ``SDF_RANGETYPE``\  subdevice flag is set.  Otherwise, the arrays they point to
must be at least as long as the number of channels.

.. _`comedi_rangeinfo`:

struct comedi_rangeinfo
=======================

.. c:type:: struct comedi_rangeinfo

    used to retrieve the range table for a channel

.. _`comedi_rangeinfo.definition`:

Definition
----------

.. code-block:: c

    struct comedi_rangeinfo {
        unsigned int range_type;
        void __user *range_ptr;
    }

.. _`comedi_rangeinfo.members`:

Members
-------

range_type
    Encodes subdevice index (bits 27:24), channel index
    (bits 23:16) and range table length (bits 15:0).

range_ptr
    Pointer to array of \ ``struct``\  comedi_krange to be filled
    in with the range table for the channel or subdevice.

.. _`comedi_rangeinfo.description`:

Description
-----------

This is used with the \ ``COMEDI_RANGEINFO``\  ioctl to retrieve the range table
for a specific channel (if the subdevice has the \ ``SDF_RANGETYPE``\  flag set to
indicate that the range table depends on the channel), or for the subdevice
as a whole (if the \ ``SDF_RANGETYPE``\  flag is clear, indicating the range table
is shared by all channels).

The \ ``range_type``\  value is an input to the ioctl and comes from a previous
use of the \ ``COMEDI_SUBDINFO``\  ioctl (if the \ ``SDF_RANGETYPE``\  flag is clear),
or the \ ``COMEDI_CHANINFO``\  ioctl (if the \ ``SDF_RANGETYPE``\  flag is set).

.. _`comedi_krange`:

struct comedi_krange
====================

.. c:type:: struct comedi_krange

    describes a range in a range table

.. _`comedi_krange.definition`:

Definition
----------

.. code-block:: c

    struct comedi_krange {
        int min;
        int max;
        unsigned int flags;
    }

.. _`comedi_krange.members`:

Members
-------

min
    Minimum value in millionths (1e-6) of a unit.

max
    Maximum value in millionths (1e-6) of a unit.

flags
    Indicates the units (in bits 7:0) OR'ed with optional flags.

.. _`comedi_krange.description`:

Description
-----------

A range table is associated with a single channel, or with all channels in a
subdevice, and a list of one or more ranges.  A \ ``struct``\  comedi_krange
describes the physical range of units for one of those ranges.  Sample
values in COMEDI are unsigned from \ ``0``\  up to some 'maxdata' value.  The
mapping from sample values to physical units is assumed to be nomimally
linear (for the purpose of describing the range), with sample value \ ``0``\ 
mapping to \ ``min``\ , and the 'maxdata' sample value mapping to \ ``max``\ .

The currently defined units are \ ``UNIT_volt``\  (%0), \ ``UNIT_mA``\  (%1), and
\ ``UNIT_none``\  (%2).  The \ ``min``\  and \ ``max``\  values are the physical range multiplied
by 1e6, so a \ ``max``\  value of \ ``1000000``\  (with \ ``UNIT_volt``\ ) represents a maximal
value of 1 volt.

The only defined flag value is \ ``RF_EXTERNAL``\  (%0x100), indicating that the
the range needs to be multiplied by an external reference.

.. _`comedi_subdinfo`:

struct comedi_subdinfo
======================

.. c:type:: struct comedi_subdinfo

    used to retrieve information about a subdevice

.. _`comedi_subdinfo.definition`:

Definition
----------

.. code-block:: c

    struct comedi_subdinfo {
        unsigned int type;
        unsigned int n_chan;
        unsigned int subd_flags;
        unsigned int timer_type;
        unsigned int len_chanlist;
        unsigned int maxdata;
        unsigned int flags;
        unsigned int range_type;
        unsigned int settling_time_0;
        unsigned int insn_bits_support;
        unsigned int unused[8];
    }

.. _`comedi_subdinfo.members`:

Members
-------

type
    Type of subdevice from \ :c:type:`enum comedi_subdevice_type <comedi_subdevice_type>`\ .

n_chan
    Number of channels the subdevice supports.

subd_flags
    A mixture of static and dynamic flags describing
    aspects of the subdevice and its current state.

timer_type
    Timer type.  Always set to \ ``5``\  ("nanosecond timer").

len_chanlist
    Maximum length of a channel list if the subdevice
    supports asynchronous acquisition commands.

maxdata
    Maximum sample value for all channels if the
    \ ``SDF_MAXDATA``\  subdevice flag is clear.

flags
    Channel flags for all channels if the \ ``SDF_FLAGS``\ 
    subdevice flag is clear.

range_type
    The range type for all channels if the \ ``SDF_RANGETYPE``\ 
    subdevice flag is clear.  Encodes the subdevice index
    (bits 27:24), a dummy channel index \ ``0``\  (bits 23:16),
    and the range table length (bits 15:0).

settling_time_0
    Not used.

insn_bits_support
    Set to \ ``COMEDI_SUPPORTED``\  if the subdevice supports the
    \ ``INSN_BITS``\  instruction, or to \ ``COMEDI_UNSUPPORTED``\  if it
    does not.

unused
    Reserved for future use.

.. _`comedi_subdinfo.description`:

Description
-----------

This is used with the \ ``COMEDI_SUBDINFO``\  ioctl which copies an array of
\ :c:type:`struct comedi_subdinfo <comedi_subdinfo>`\  back to user space, with one element per subdevice.
Use of this requires knowledge of the number of subdevices obtained from
the \ ``COMEDI_DEVINFO``\  ioctl.

These are the \ ``subd_flags``\  values that may be ORed together...

\ ``SDF_BUSY``\  - the subdevice is busy processing an asynchronous command or a
synchronous instruction.

\ ``SDF_BUSY_OWNER``\  - the subdevice is busy processing an asynchronous
acquisition command started on the current file object (the file object
issuing the \ ``COMEDI_SUBDINFO``\  ioctl).

\ ``SDF_LOCKED``\  - the subdevice is locked by a \ ``COMEDI_LOCK``\  ioctl.

\ ``SDF_LOCK_OWNER``\  - the subdevice is locked by a \ ``COMEDI_LOCK``\  ioctl from the
current file object.

\ ``SDF_MAXDATA``\  - maximum sample values are channel-specific.

\ ``SDF_FLAGS``\  - channel flags are channel-specific.

\ ``SDF_RANGETYPE``\  - range types are channel-specific.

\ ``SDF_PWM_COUNTER``\  - PWM can switch off automatically.

\ ``SDF_PWM_HBRIDGE``\  - or PWM is signed (H-bridge).

\ ``SDF_CMD``\  - the subdevice supports asynchronous commands.

\ ``SDF_SOFT_CALIBRATED``\  - the subdevice uses software calibration.

\ ``SDF_CMD_WRITE``\  - the subdevice supports asynchronous commands in the output
("write") direction.

\ ``SDF_CMD_READ``\  - the subdevice supports asynchronous commands in the input
("read") direction.

\ ``SDF_READABLE``\  - the subdevice is readable (e.g. analog input).

\ ``SDF_WRITABLE``\  (aliased as \ ``SDF_WRITEABLE``\ ) - the subdevice is writable (e.g.
analog output).

\ ``SDF_INTERNAL``\  - the subdevice has no externally visible lines.

\ ``SDF_GROUND``\  - the subdevice can use ground as an analog reference.

\ ``SDF_COMMON``\  - the subdevice can use a common analog reference.

\ ``SDF_DIFF``\  - the subdevice can use differential inputs (or outputs).

\ ``SDF_OTHER``\  - the subdevice can use some other analog reference.

\ ``SDF_DITHER``\  - the subdevice can do dithering.

\ ``SDF_DEGLITCH``\  - the subdevice can do deglitching.

\ ``SDF_MMAP``\  - this is never set.

\ ``SDF_RUNNING``\  - an asynchronous command is still running.

\ ``SDF_LSAMPL``\  - the subdevice uses "long" (32-bit) samples (for asynchronous
command data).

\ ``SDF_PACKED``\  - the subdevice packs several DIO samples into a single sample
(for asynchronous command data).

No "channel flags" (@flags) values are currently defined.

.. _`comedi_devinfo`:

struct comedi_devinfo
=====================

.. c:type:: struct comedi_devinfo

    used to retrieve information about a COMEDI device

.. _`comedi_devinfo.definition`:

Definition
----------

.. code-block:: c

    struct comedi_devinfo {
        unsigned int version_code;
        unsigned int n_subdevs;
        char driver_name[COMEDI_NAMELEN];
        char board_name[COMEDI_NAMELEN];
        int read_subdevice;
        int write_subdevice;
        int unused[30];
    }

.. _`comedi_devinfo.members`:

Members
-------

version_code
    COMEDI version code.

n_subdevs
    Number of subdevices the device has.

driver_name
    Null-terminated COMEDI driver name.

board_name
    Null-terminated COMEDI board name.

read_subdevice
    Index of the current "read" subdevice (%-1 if none).

write_subdevice
    Index of the current "write" subdevice (%-1 if none).

unused
    Reserved for future use.

.. _`comedi_devinfo.description`:

Description
-----------

This is used with the \ ``COMEDI_DEVINFO``\  ioctl to get basic information about
the device.

.. _`comedi_devconfig`:

struct comedi_devconfig
=======================

.. c:type:: struct comedi_devconfig

    used to configure a legacy COMEDI device

.. _`comedi_devconfig.definition`:

Definition
----------

.. code-block:: c

    struct comedi_devconfig {
        char board_name[COMEDI_NAMELEN];
        int options[COMEDI_NDEVCONFOPTS];
    }

.. _`comedi_devconfig.members`:

Members
-------

board_name
    Null-terminated string specifying the type of board
    to configure.

options
    An array of integer configuration options.

.. _`comedi_devconfig.description`:

Description
-----------

This is used with the \ ``COMEDI_DEVCONFIG``\  ioctl to configure a "legacy" COMEDI
device, such as an ISA card.  Not all COMEDI drivers support this.  Those
that do either expect the specified board name to match one of a list of
names registered with the COMEDI core, or expect the specified board name
to match the COMEDI driver name itself.  The configuration options are
handled in a driver-specific manner.

.. _`comedi_bufconfig`:

struct comedi_bufconfig
=======================

.. c:type:: struct comedi_bufconfig

    used to set or get buffer size for a subdevice

.. _`comedi_bufconfig.definition`:

Definition
----------

.. code-block:: c

    struct comedi_bufconfig {
        unsigned int subdevice;
        unsigned int flags;
        unsigned int maximum_size;
        unsigned int size;
        unsigned int unused[4];
    }

.. _`comedi_bufconfig.members`:

Members
-------

subdevice
    Subdevice index.

flags
    Not used.

maximum_size
    Maximum allowed buffer size.

size
    Buffer size.

unused
    Reserved for future use.

.. _`comedi_bufconfig.description`:

Description
-----------

This is used with the \ ``COMEDI_BUFCONFIG``\  ioctl to get or configure the
maximum buffer size and current buffer size for a COMEDI subdevice that
supports asynchronous commands.  If the subdevice does not support
asynchronous commands, \ ``maximum_size``\  and \ ``size``\  are ignored and set to 0.

On ioctl input, non-zero values of \ ``maximum_size``\  and \ ``size``\  specify a
new maximum size and new current size (in bytes), respectively.  These
will by rounded up to a multiple of \ ``PAGE_SIZE``\ .  Specifying a new maximum
size requires admin capabilities.

On ioctl output, \ ``maximum_size``\  and \ ``size``\  and set to the current maximum
buffer size and current buffer size, respectively.

.. _`comedi_bufinfo`:

struct comedi_bufinfo
=====================

.. c:type:: struct comedi_bufinfo

    used to manipulate buffer position for a subdevice

.. _`comedi_bufinfo.definition`:

Definition
----------

.. code-block:: c

    struct comedi_bufinfo {
        unsigned int subdevice;
        unsigned int bytes_read;
        unsigned int buf_write_ptr;
        unsigned int buf_read_ptr;
        unsigned int buf_write_count;
        unsigned int buf_read_count;
        unsigned int bytes_written;
        unsigned int unused[4];
    }

.. _`comedi_bufinfo.members`:

Members
-------

subdevice
    Subdevice index.

bytes_read
    Specify amount to advance read position for an
    asynchronous command in the input ("read") direction.

buf_write_ptr
    Current write position (index) within the buffer.

buf_read_ptr
    Current read position (index) within the buffer.

buf_write_count
    Total amount written, modulo 2^32.

buf_read_count
    Total amount read, modulo 2^32.

bytes_written
    Specify amount to advance write position for an
    asynchronous command in the output ("write") direction.

unused
    Reserved for future use.

.. _`comedi_bufinfo.description`:

Description
-----------

This is used with the \ ``COMEDI_BUFINFO``\  ioctl to optionally advance the
current read or write position in an asynchronous acquisition data buffer,
and to get the current read and write positions in the buffer.

.. This file was automatic generated / don't edit.

