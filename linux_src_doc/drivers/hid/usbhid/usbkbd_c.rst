.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/hid/usbhid/usbkbd.c

.. _`usb_kbd`:

struct usb_kbd
==============

.. c:type:: struct usb_kbd

    state of each attached keyboard

.. _`usb_kbd.definition`:

Definition
----------

.. code-block:: c

    struct usb_kbd {
        struct input_dev *dev;
        struct usb_device *usbdev;
        unsigned char old;
        struct urb *irq;
        struct urb * *led;
        unsigned char newleds;
        char name;
        char phys;
        unsigned char *new;
        struct usb_ctrlrequest *cr;
        unsigned char *leds;
        dma_addr_t new_dma;
        dma_addr_t leds_dma;
        spinlock_t leds_lock;
        bool led_urb_submitted;
    }

.. _`usb_kbd.members`:

Members
-------

dev
    input device associated with this keyboard

usbdev
    usb device associated with this keyboard

old
    data received in the past from the \ ``irq``\  URB representing which
    keys were pressed. By comparing with the current list of keys
    that are pressed, we are able to see key releases.

irq
    URB for receiving a list of keys that are pressed when a
    new key is pressed or a key that was pressed is released.

led
    URB for sending LEDs (e.g. numlock, ...)

newleds
    data that will be sent with the \ ``led``\  URB representing which LEDs

name
    Name of the keyboard. \ ``dev``\ 's name field points to this buffer

phys
    Physical path of the keyboard. \ ``dev``\ 's phys field points to this
    buffer

new
    Buffer for the \ ``irq``\  URB

cr
    Control request for \ ``led``\  URB

leds
    Buffer for the \ ``led``\  URB

new_dma
    DMA address for \ ``irq``\  URB

leds_dma
    DMA address for \ ``led``\  URB

leds_lock
    spinlock that protects \ ``leds``\ , \ ``newleds``\ , and \ ``led_urb_submitted``\ 

led_urb_submitted
    indicates whether \ ``led``\  is in progress, i.e. it has been
    submitted and its completion handler has not returned yet
    without resubmitting \ ``led``\ 

.. This file was automatic generated / don't edit.

