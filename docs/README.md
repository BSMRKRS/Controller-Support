# Controller-Support

Welcome to Controller Support!

## Run

Host(Robot):

- Choose host file
  - ax.py (for ax-12 servos and only python3 compatible)
  - RoboPi.py (for RoboPi hat servos and compatible with python2 & python3)

```bash
cd host
python <host.py>
```

Client(Laptop):

```bash
python controller.py <host_ip>
```

## Setup

- Refer to bsmLib's [controller documentation](https://github.com/BSMRKRS/bsmLib/blob/master/docs/controller.md) for driver installation
- Clone repo to client(laptop) & host(robot)

```bash
git clone https://github.com/BSMRKRS/Controller-Support.git
```

## Dependencies

- [bsmLib](https://github.com/BSMRKRS/bsmLib/)
- [pyax12](https://github.com/jeremiedecock/pyax12) - Only need for ax-12

## License

[License](/docs/LICENSE)
