.. -*- coding: utf-8; mode: rst -*-

.. _netdev:

======================
Network device support
======================


Driver Support
==============


.. toctree::
    :maxdepth: 1

    API-dev-add-pack
    API---dev-remove-pack
    API-dev-remove-pack
    API-dev-add-offload
    API-dev-remove-offload
    API-netdev-boot-setup-check
    API-dev-get-iflink
    API-dev-fill-metadata-dst
    API---dev-get-by-name
    API-dev-get-by-name-rcu
    API-dev-get-by-name
    API---dev-get-by-index
    API-dev-get-by-index-rcu
    API-dev-get-by-index
    API-dev-getbyhwaddr-rcu
    API---dev-get-by-flags
    API-dev-valid-name
    API-dev-alloc-name
    API-netdev-features-change
    API-netdev-state-change
    API-netdev-notify-peers
    API-dev-open
    API-dev-close
    API-dev-disable-lro
    API-register-netdevice-notifier
    API-unregister-netdevice-notifier
    API-call-netdevice-notifiers
    API-dev-forward-skb
    API-netif-set-real-num-rx-queues
    API-netif-get-num-default-rss-queues
    API-netif-wake-subqueue
    API-netif-device-detach
    API-netif-device-attach
    API-skb-mac-gso-segment
    API---skb-gso-segment
    API-dev-loopback-xmit
    API-rps-may-expire-flow
    API-netif-rx
    API-netdev-rx-handler-register
    API-netdev-rx-handler-unregister
    API-netif-receive-skb
    API---napi-schedule
    API---napi-schedule-irqoff
    API-netdev-has-upper-dev
    API-netdev-master-upper-dev-get
    API-netdev-upper-get-next-dev-rcu
    API-netdev-all-upper-get-next-dev-rcu
    API-netdev-lower-get-next-private
    API-netdev-lower-get-next-private-rcu
    API-netdev-lower-get-next
    API-netdev-lower-get-first-private-rcu
    API-netdev-master-upper-dev-get-rcu
    API-netdev-upper-dev-link
    API-netdev-master-upper-dev-link
    API-netdev-upper-dev-unlink
    API-netdev-bonding-info-change
    API-netdev-lower-state-changed
    API-dev-set-promiscuity
    API-dev-set-allmulti
    API-dev-get-flags
    API-dev-change-flags
    API-dev-set-mtu
    API-dev-set-group
    API-dev-set-mac-address
    API-dev-change-carrier
    API-dev-get-phys-port-id
    API-dev-get-phys-port-name
    API-dev-change-proto-down
    API-netdev-update-features
    API-netdev-change-features
    API-netif-stacked-transfer-operstate
    API-register-netdevice
    API-init-dummy-netdev
    API-register-netdev
    API-dev-get-stats
    API-alloc-netdev-mqs
    API-free-netdev
    API-synchronize-net
    API-unregister-netdevice-queue
    API-unregister-netdevice-many
    API-unregister-netdev
    API-dev-change-net-namespace
    API-netdev-increment-features
    API-eth-header
    API-eth-get-headlen
    API-eth-type-trans
    API-eth-header-parse
    API-eth-header-cache
    API-eth-header-cache-update
    API-eth-prepare-mac-addr-change
    API-eth-commit-mac-addr-change
    API-eth-mac-addr
    API-eth-change-mtu
    API-ether-setup
    API-alloc-etherdev-mqs
    API-netif-carrier-on
    API-netif-carrier-off
    API-is-link-local-ether-addr
    API-is-zero-ether-addr
    API-is-multicast-ether-addr
    API-is-local-ether-addr
    API-is-broadcast-ether-addr
    API-is-unicast-ether-addr
    API-is-valid-ether-addr
    API-eth-proto-is-802-3
    API-eth-random-addr
    API-eth-broadcast-addr
    API-eth-zero-addr
    API-eth-hw-addr-random
    API-ether-addr-copy
    API-eth-hw-addr-inherit
    API-ether-addr-equal
    API-ether-addr-equal-64bits
    API-ether-addr-equal-unaligned
    API-is-etherdev-addr
    API-compare-ether-header
    API-eth-skb-pad
    API-napi-schedule-prep
    API-napi-schedule
    API-napi-schedule-irqoff
    API-napi-complete
    API-napi-enable
    API-napi-synchronize
    API-enum-netdev-priv-flags
    API-struct-net-device
    API-netdev-priv
    API-netif-tx-napi-add
    API-netif-start-queue
    API-netif-wake-queue
    API-netif-stop-queue
    API-netif-queue-stopped
    API-netdev-txq-bql-enqueue-prefetchw
    API-netdev-txq-bql-complete-prefetchw
    API-netdev-sent-queue
    API-netdev-completed-queue
    API-netdev-reset-queue
    API-netdev-cap-txqueue
    API-netif-running
    API-netif-start-subqueue
    API-netif-stop-subqueue
    API---netif-subqueue-stopped
    API-netif-is-multiqueue
    API-dev-put
    API-dev-hold
    API-netif-carrier-ok
    API-netif-dormant-on
    API-netif-dormant-off
    API-netif-dormant
    API-netif-oper-up
    API-netif-device-present
    API-netif-tx-lock
    API---dev-uc-sync
    API---dev-uc-unsync
    API---dev-mc-sync
    API---dev-mc-unsync


PHY Support
===========


.. toctree::
    :maxdepth: 1

    API-phy-print-status
    API-phy-ethtool-sset
    API-phy-mii-ioctl
    API-phy-start-aneg
    API-phy-start-interrupts
    API-phy-stop-interrupts
    API-phy-stop
    API-phy-start
    API-phy-read-mmd-indirect
    API-phy-write-mmd-indirect
    API-phy-init-eee
    API-phy-get-eee-err
    API-phy-ethtool-get-eee
    API-phy-ethtool-set-eee
    API-phy-clear-interrupt
    API-phy-config-interrupt
    API-phy-aneg-done
    API-phy-find-setting
    API-phy-find-valid
    API-phy-check-valid
    API-phy-sanitize-settings
    API-phy-start-machine
    API-phy-stop-machine
    API-phy-error
    API-phy-interrupt
    API-phy-enable-interrupts
    API-phy-disable-interrupts
    API-phy-change
    API-phy-state-machine
    API-phy-register-fixup
    API-get-phy-device
    API-phy-device-register
    API-phy-device-remove
    API-phy-find-first
    API-phy-connect-direct
    API-phy-connect
    API-phy-disconnect
    API-phy-attach-direct
    API-phy-attach
    API-phy-detach
    API-genphy-setup-forced
    API-genphy-restart-aneg
    API-genphy-config-aneg
    API-genphy-aneg-done
    API-genphy-update-link
    API-genphy-read-status
    API-genphy-soft-reset
    API-phy-driver-register
    API-get-phy-c45-ids
    API-get-phy-id
    API-phy-prepare-link
    API-phy-poll-reset
    API-genphy-config-advert
    API-phy-probe
    API-mdiobus-alloc-size
    API-devm-mdiobus-alloc-size
    API-devm-mdiobus-free
    API-of-mdio-find-bus
    API---mdiobus-register
    API-mdiobus-free
    API-mdiobus-scan
    API-mdiobus-read-nested
    API-mdiobus-read
    API-mdiobus-write-nested
    API-mdiobus-write
    API-mdiobus-release
    API-mdio-bus-match




.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
