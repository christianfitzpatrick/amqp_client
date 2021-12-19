# amqp_client

A Python client library providing high-level bindings for communicating with an AMQP message broker.

The general structure is as follows:

## `amqp_core`
Provides high-level mappings to the protocol methods defined in the AMQP specification's command architecture.
This package serves to provide a user-friendly API for developing AMQP client applications while abstracting away the transport details.

## `amqp_transport`
The wire-level implementation of the protocol. AMQP commands between a client and server (broker) are issued via remote procedure calls.
These RPCs are marshaled into data structures called *frames* which adhere to a set binary protocol.
The goal of this package is to facilitate the generation of 'ready-to-go' RPC frames that correspond to the commands provided by the `amqp_core` package.
As such, this package serves to back those abstractions and is generally not of interest to the end user.
