
.. _API---handle-domain-irq:

===================
__handle_domain_irq
===================

*man __handle_domain_irq(9)*

*4.6.0-rc1*

Invoke the handler for a HW irq belonging to a domain


Synopsis
========

.. c:function:: int __handle_domain_irq( struct irq_domain * domain, unsigned int hwirq, bool lookup, struct pt_regs * regs )

Arguments
=========

``domain``
    The domain where to perform the lookup

``hwirq``
    The HW irq number to convert to a logical one

``lookup``
    Whether to perform the domain lookup or not

``regs``
    Register file coming from the low-level handling code


Returns
=======

0 on success, or -EINVAL if conversion has failed
