.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/i2c/busses/i2c-stm32f7.c

.. _`stm32f7_i2c_spec`:

struct stm32f7_i2c_spec
=======================

.. c:type:: struct stm32f7_i2c_spec

    private i2c specification timing

.. _`stm32f7_i2c_spec.definition`:

Definition
----------

.. code-block:: c

    struct stm32f7_i2c_spec {
        u32 rate;
        u32 rate_min;
        u32 rate_max;
        u32 fall_max;
        u32 rise_max;
        u32 hddat_min;
        u32 vddat_max;
        u32 sudat_min;
        u32 l_min;
        u32 h_min;
    }

.. _`stm32f7_i2c_spec.members`:

Members
-------

rate
    I2C bus speed (Hz)

rate_min
    80% of I2C bus speed (Hz)

rate_max
    100% of I2C bus speed (Hz)

fall_max
    Max fall time of both SDA and SCL signals (ns)

rise_max
    Max rise time of both SDA and SCL signals (ns)

hddat_min
    Min data hold time (ns)

vddat_max
    Max data valid time (ns)

sudat_min
    Min data setup time (ns)

l_min
    Min low period of the SCL clock (ns)

h_min
    Min high period of the SCL clock (ns)

.. _`stm32f7_i2c_setup`:

struct stm32f7_i2c_setup
========================

.. c:type:: struct stm32f7_i2c_setup

    private I2C timing setup parameters

.. _`stm32f7_i2c_setup.definition`:

Definition
----------

.. code-block:: c

    struct stm32f7_i2c_setup {
        enum stm32_i2c_speed speed;
        u32 speed_freq;
        u32 clock_src;
        u32 rise_time;
        u32 fall_time;
        u8 dnf;
        bool analog_filter;
    }

.. _`stm32f7_i2c_setup.members`:

Members
-------

speed
    I2C speed mode (standard, Fast Plus)

speed_freq
    I2C speed frequency  (Hz)

clock_src
    I2C clock source frequency (Hz)

rise_time
    Rise time (ns)

fall_time
    Fall time (ns)

dnf
    Digital filter coefficient (0-16)

analog_filter
    Analog filter delay (On/Off)

.. _`stm32f7_i2c_timings`:

struct stm32f7_i2c_timings
==========================

.. c:type:: struct stm32f7_i2c_timings

    private I2C output parameters

.. _`stm32f7_i2c_timings.definition`:

Definition
----------

.. code-block:: c

    struct stm32f7_i2c_timings {
        struct list_head node;
        u8 presc;
        u8 scldel;
        u8 sdadel;
        u8 sclh;
        u8 scll;
    }

.. _`stm32f7_i2c_timings.members`:

Members
-------

node
    List entry

presc
    Prescaler value

scldel
    Data setup time

sdadel
    Data hold time

sclh
    SCL high period (master mode)

scll
    SCL low period (master mode)

.. _`stm32f7_i2c_msg`:

struct stm32f7_i2c_msg
======================

.. c:type:: struct stm32f7_i2c_msg

    client specific data

.. _`stm32f7_i2c_msg.definition`:

Definition
----------

.. code-block:: c

    struct stm32f7_i2c_msg {
        u16 addr;
        u32 count;
        u8 *buf;
        int result;
        bool stop;
        bool smbus;
        int size;
        char read_write;
        u8 smbus_buf[I2C_SMBUS_BLOCK_MAX + 3] __aligned(4);
    }

.. _`stm32f7_i2c_msg.members`:

Members
-------

addr
    8-bit or 10-bit slave addr, including r/w bit

count
    number of bytes to be transferred

buf
    data buffer

result
    result of the transfer

stop
    last I2C msg to be sent, i.e. STOP to be generated

smbus
    boolean to know if the I2C IP is used in SMBus mode

size
    type of SMBus protocol

read_write
    direction of SMBus protocol
    SMBus block read and SMBus block write - block read process call protocols

smbus_buf
    buffer to be used for SMBus protocol transfer. It will
    contain a maximum of 32 bytes of data + byte command + byte count + PEC
    This buffer has to be 32-bit aligned to be compliant with memory address
    register in DMA mode.

.. _`stm32f7_i2c_dev`:

struct stm32f7_i2c_dev
======================

.. c:type:: struct stm32f7_i2c_dev

    private data of the controller

.. _`stm32f7_i2c_dev.definition`:

Definition
----------

.. code-block:: c

    struct stm32f7_i2c_dev {
        struct i2c_adapter adap;
        struct device *dev;
        void __iomem *base;
        struct completion complete;
        struct clk *clk;
        int speed;
        struct i2c_msg *msg;
        unsigned int msg_num;
        unsigned int msg_id;
        struct stm32f7_i2c_msg f7_msg;
        struct stm32f7_i2c_setup setup;
        struct stm32f7_i2c_timings timing;
        struct i2c_client *slave[STM32F7_I2C_MAX_SLAVE];
        struct i2c_client *slave_running;
        u32 slave_dir;
        bool master_mode;
        struct stm32_i2c_dma *dma;
        bool use_dma;
    }

.. _`stm32f7_i2c_dev.members`:

Members
-------

adap
    I2C adapter for this controller

dev
    device for this controller

base
    virtual memory area

complete
    completion of I2C message

clk
    hw i2c clock

speed
    I2C clock frequency of the controller. Standard, Fast or Fast+

msg
    Pointer to data to be written

msg_num
    number of I2C messages to be executed

msg_id
    message identifiant

f7_msg
    customized i2c msg for driver usage

setup
    I2C timing input setup

timing
    I2C computed timings

slave
    list of slave devices registered on the I2C bus

slave_running
    slave device currently used

slave_dir
    transfer direction for the current slave device

master_mode
    boolean to know in which mode the I2C is running (master or
    slave)

dma
    dma data

use_dma
    boolean to know if dma is used in the current transfer

.. This file was automatic generated / don't edit.

