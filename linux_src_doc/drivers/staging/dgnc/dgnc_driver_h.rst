.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/dgnc/dgnc_driver.h

.. _`board_ops`:

struct board_ops
================

.. c:type:: struct board_ops

    Per board operations.

.. _`board_ops.definition`:

Definition
----------

.. code-block:: c

    struct board_ops {
        void (*tasklet)(unsigned long data);
        irqreturn_t (*intr)(int irq, void *voidbrd);
        void (*uart_init)(struct channel_t *ch);
        void (*uart_off)(struct channel_t *ch);
        int (*drain)(struct tty_struct *tty, uint seconds);
        void (*param)(struct tty_struct *tty);
        void (*vpd)(struct dgnc_board *brd);
        void (*assert_modem_signals)(struct channel_t *ch);
        void (*flush_uart_write)(struct channel_t *ch);
        void (*flush_uart_read)(struct channel_t *ch);
        void (*disable_receiver)(struct channel_t *ch);
        void (*enable_receiver)(struct channel_t *ch);
        void (*send_break)(struct channel_t *ch, int);
        void (*send_start_character)(struct channel_t *ch);
        void (*send_stop_character)(struct channel_t *ch);
        void (*copy_data_from_queue_to_uart)(struct channel_t *ch);
        uint (*get_uart_bytes_left)(struct channel_t *ch);
        void (*send_immediate_char)(struct channel_t *ch, unsigned char);
    }

.. _`board_ops.members`:

Members
-------

tasklet
    *undescribed*

intr
    *undescribed*

uart_init
    *undescribed*

uart_off
    *undescribed*

drain
    *undescribed*

param
    *undescribed*

vpd
    *undescribed*

assert_modem_signals
    *undescribed*

flush_uart_write
    *undescribed*

flush_uart_read
    *undescribed*

disable_receiver
    *undescribed*

enable_receiver
    *undescribed*

send_break
    *undescribed*

send_start_character
    *undescribed*

send_stop_character
    *undescribed*

copy_data_from_queue_to_uart
    *undescribed*

get_uart_bytes_left
    *undescribed*

send_immediate_char
    *undescribed*

.. _`dgnc_board`:

struct dgnc_board
=================

.. c:type:: struct dgnc_board

    Per board information.

.. _`dgnc_board.definition`:

Definition
----------

.. code-block:: c

    struct dgnc_board {
        int boardnum;
        int type;
        char *name;
        struct pci_dev *pdev;
        unsigned long bd_flags;
        u16 vendor;
        u16 device;
        u16 subvendor;
        u16 subdevice;
        unsigned char rev;
        uint pci_bus;
        uint pci_slot;
        uint maxports;
        unsigned char dvid;
        unsigned char vpd[128];
        unsigned char serial_num[20];
        spinlock_t bd_lock;
        spinlock_t bd_intr_lock;
        uint state;
        wait_queue_head_t state_wait;
        struct tasklet_struct helper_tasklet;
        uint nasync;
        uint irq;
        ulong membase;
        ulong membase_end;
        u8 __iomem *re_map_membase;
        ulong iobase;
        ulong iobase_end;
        uint bd_uart_offset;
        struct channel_t  *channels[MAXPORTS];
        struct tty_driver *serial_driver;
        char serial_name[200];
        struct tty_driver *print_driver;
        char print_name[200];
        u16 dpatype;
        u16 dpastatus;
        uint bd_dividend;
        struct board_ops *bd_ops;
        struct proc_dir_entry *proc_entry_pointer;
        struct dgnc_proc_entry *dgnc_board_table;
    }

.. _`dgnc_board.members`:

Members
-------

boardnum
    Board number (0 - 32).

type
    Type of board.

name
    Product name.

pdev
    Pointer to the pci_dev structure.

bd_flags
    Board flags.

vendor
    PCI vendor ID.

device
    PCI device ID.

subvendor
    PCI subsystem vendor ID.

subdevice
    PCI subsystem device ID.

rev
    PCI revision ID.

pci_bus
    PCI bus value.

pci_slot
    PCI slot value.

maxports
    Maximum ports this board can handle.

dvid
    Board specific device ID.

vpd
    VPD of this board, if found.

serial_num
    Serial number of this board, if found in VPD.

bd_lock
    Used to protect board.

bd_intr_lock
    Protect poller tasklet and interrupt routine from each other.

state
    State of the card.

state_wait
    Queue to sleep on for state change.

helper_tasklet
    Poll helper tasklet.

nasync
    Number of ports on card.

irq
    Interrupt request number.

membase
    Start of base memory of the card.

membase_end
    End of base memory of the card.

re_map_membase
    *undescribed*

iobase
    Start of IO base of the card.

iobase_end
    End of IO base of the card.

bd_uart_offset
    Space between each UART.

channels
    array of pointers to our channels.

serial_driver
    Pointer to the serial driver.

serial_name
    Serial driver name.

print_driver
    *undescribed*

print_name
    Print driver name.

dpatype
    Board type as defined by DPA.

dpastatus
    Board status as defined by DPA.

bd_dividend
    Board/UART's specific dividend.

bd_ops
    Pointer to board operations structure.

proc_entry_pointer
    Proc/<board> entry

dgnc_board_table
    Proc/<board> entry

.. _`un_t`:

struct un_t
===========

.. c:type:: struct un_t

    terminal or printer unit

.. _`un_t.definition`:

Definition
----------

.. code-block:: c

    struct un_t {
        struct channel_t *un_ch;
        ulong un_time;
        uint un_type;
        uint un_open_count;
        struct tty_struct *un_tty;
        uint un_flags;
        wait_queue_head_t un_flags_wait;
        uint un_dev;
        struct device *un_sysfs;
    }

.. _`un_t.members`:

Members
-------

un_ch
    *undescribed*

un_time
    *undescribed*

un_type
    *undescribed*

un_open_count
    Counter of opens to port.

un_tty
    Pointer to unit tty structure.

un_flags
    Unit flags.

un_flags_wait
    Place to sleep to wait on unit.

un_dev
    Minor device number.

un_sysfs
    *undescribed*

.. _`channel_t`:

struct channel_t
================

.. c:type:: struct channel_t

    Channel information.

.. _`channel_t.definition`:

Definition
----------

.. code-block:: c

    struct channel_t {
        struct dgnc_board *ch_bd;
        struct digi_t ch_digi;
        struct un_t ch_tun;
        struct un_t ch_pun;
        spinlock_t ch_lock;
        wait_queue_head_t ch_flags_wait;
        uint ch_portnum;
        uint ch_open_count;
        uint ch_flags;
        ulong ch_close_delay;
        ulong ch_cpstime;
        tcflag_t ch_c_iflag;
        tcflag_t ch_c_cflag;
        tcflag_t ch_c_oflag;
        tcflag_t ch_c_lflag;
        unsigned char ch_stopc;
        unsigned char ch_startc;
        uint ch_old_baud;
        uint ch_custom_speed;
        uint ch_wopen;
        unsigned char ch_mostat;
        unsigned char ch_mistat;
        struct neo_uart_struct __iomem *ch_neo_uart;
        struct cls_uart_struct __iomem *ch_cls_uart;
        unsigned char ch_cached_lsr;
        unsigned char *ch_rqueue;
        ushort ch_r_head;
        ushort ch_r_tail;
        unsigned char *ch_equeue;
        ushort ch_e_head;
        ushort ch_e_tail;
        unsigned char *ch_wqueue;
        ushort ch_w_head;
        ushort ch_w_tail;
        ulong ch_rxcount;
        ulong ch_txcount;
        unsigned char ch_r_tlevel;
        unsigned char ch_t_tlevel;
        unsigned char ch_r_watermark;
        ulong ch_stop_sending_break;
        uint ch_stops_sent;
        ulong ch_err_parity;
        ulong ch_err_frame;
        ulong ch_err_break;
        ulong ch_err_overrun;
        ulong ch_xon_sends;
        ulong ch_xoff_sends;
        struct proc_dir_entry *proc_entry_pointer;
        struct dgnc_proc_entry *dgnc_channel_table;
    }

.. _`channel_t.members`:

Members
-------

ch_bd
    Transparent print structure.

ch_digi
    *undescribed*

ch_tun
    Terminal unit information.

ch_pun
    Printer unit information.

ch_lock
    Provide for serialization.

ch_flags_wait
    Channel flags wait queue.

ch_portnum
    Port number, 0 offset.

ch_open_count
    Open count.

ch_flags
    Channel flags.

ch_close_delay
    How long we should drop RTS/DTR for.

ch_cpstime
    Time for CPS calculations.

ch_c_iflag
    Channel iflags.

ch_c_cflag
    Channel cflags.

ch_c_oflag
    Channel oflags.

ch_c_lflag
    Channel lflags.

ch_stopc
    Stop character.

ch_startc
    Start character.

ch_old_baud
    Cache of the current baud rate.

ch_custom_speed
    Custom baud rate, if set.

ch_wopen
    Waiting for open process count.

ch_mostat
    FEP output modem status.

ch_mistat
    FEP input modem status.

ch_neo_uart
    *undescribed*

ch_cls_uart
    Pointer to the mapped cls UART struct

ch_cached_lsr
    Cached value of the LSR register.

ch_rqueue
    Read queue buffer, malloc'ed.

ch_r_head
    Head location of the read queue.

ch_r_tail
    Tail location of the read queue.

ch_equeue
    Error queue buffer, malloc'ed.

ch_e_head
    Head location of the error queue.

ch_e_tail
    Tail location of the error queue.

ch_wqueue
    Write queue buffer, malloc'ed.

ch_w_head
    Head location of the write queue.

ch_w_tail
    Tail location of the write queue.

ch_rxcount
    Total of data received so far.

ch_txcount
    Total of data transmitted so far.

ch_r_tlevel
    Receive trigger level.

ch_t_tlevel
    Transmit trigger level.

ch_r_watermark
    Receive water mark.

ch_stop_sending_break
    Time we should STOP sending a break.

ch_stops_sent
    How many times I have send a stop character to try
    to stop the other guy sending.

ch_err_parity
    Count of parity

ch_err_frame
    Count of framing errors on channel.

ch_err_break
    Count of breaks on channel.

ch_err_overrun
    Count of overruns on channel.

ch_xon_sends
    Count of xons transmitted.

ch_xoff_sends
    Count of xoffs transmitted.

proc_entry_pointer
    Proc/<board>/<channel> entry.

dgnc_channel_table
    Proc/<board>/<channel> entry.

.. This file was automatic generated / don't edit.

