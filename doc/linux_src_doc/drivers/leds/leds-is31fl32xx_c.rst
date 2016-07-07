.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/leds/leds-is31fl32xx.c

.. _`is31fl32xx_chipdef`:

struct is31fl32xx_chipdef
=========================

.. c:type:: struct is31fl32xx_chipdef

    chip-specific attributes

.. _`is31fl32xx_chipdef.definition`:

Definition
----------

.. code-block:: c

    struct is31fl32xx_chipdef {
        u8 channels;
        u8 shutdown_reg;
        u8 pwm_update_reg;
        u8 global_control_reg;
        u8 reset_reg;
        u8 pwm_register_base;
        bool pwm_registers_reversed;
        u8 led_control_register_base;
        u8 enable_bits_per_led_control_register;
        int (* reset_func) (struct is31fl32xx_priv *priv);
        int (* sw_shutdown_func) (struct is31fl32xx_priv *priv, bool enable);
    }

.. _`is31fl32xx_chipdef.members`:

Members
-------

channels
    Number of LED channels

shutdown_reg
    address of Shutdown register (optional)

pwm_update_reg
    address of PWM Update register

global_control_reg
    address of Global Control register (optional)

reset_reg
    address of Reset register (optional)

pwm_register_base
    address of first PWM register

pwm_registers_reversed
    : true if PWM registers count down instead of up

led_control_register_base
    address of first LED control register (optional)

enable_bits_per_led_control_register
    number of LEDs enable bits in each

reset_func
    : pointer to reset function

sw_shutdown_func
    *undescribed*

.. _`is31fl32xx_chipdef.description`:

Description
-----------

For all optional register addresses, the sentinel value \ ``IS31FL32XX_REG_NONE``\ 
indicates that this chip has no such register.

If non-NULL, \ ``reset_func``\  will be called during probing to set all
necessary registers to a known initialization state. This is needed
for chips that do not have a \ ``reset_reg``\ .

\ ``enable_bits_per_led_control_register``\  must be >=1 if
\ ``led_control_register_base``\  != \ ``IS31FL32XX_REG_NONE``\ .

.. This file was automatic generated / don't edit.

