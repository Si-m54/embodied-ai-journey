# Embodied AI Journey

Building toward **embodied foundation models** — starting from the systems and
sim-to-real foundation that makes them work: multi-sensor perception, robot middleware,
and physical-system modeling.

## Why this repo

I'm a software engineer in industrial automation transitioning into embodied AI.
Background: multi-sensor fusion for unmanned surface vehicles (lidar + radar, target
tracking), display driver development, industrial real-time systems.

This repo tracks the transition week by week — real code, real robots, real notes.
Not tutorial exercises.

## Goal

Build toward Embodied AI foundation models — currently building the systems and
sim-to-real foundation for it.

## Progress

| Week | Focus | Output |
|---|---|---|
| W1 · 2026-11-01 | Restart, first robot simulation | `week01/` — FetchReach running (gymnasium-robotics + MuJoCo) |

## Roadmap

1. **Perception fusion & ROS 2** (W2–W9) — rebuild my USV fusion work in ROS 2
2. **3D perception** (W6–W9) — point clouds, Open3D, detection
3. **Sim2Real** (W10–W17) — Isaac Lab, domain randomization, system identification
4. **Real robot** (W18–W25) — teleoperation, ACT/Diffusion Policy, actuator modeling
5. **Paper & applications** (W26–W32) — workshop paper, then job or PhD applications

## Environment

- Python 3.11 (conda env `robot`)
- `gymnasium-robotics`, `mujoco`, `imageio`
- ROS 2 Jazzy on WSL2 (from week 2)

## Run

```bash
conda activate robot
python week01/first_robot.py
