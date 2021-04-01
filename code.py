import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots


def non_sudanese():
    s, t = np.mgrid[-1:1:200j, 0:2*np.pi:200j]
    x = (3+s*np.cos(t/2))*np.cos(t)
    y = (3+s*np.sin(t/2))*np.sin(t)
    z = s*np.sin(t/2)
    return (x, y, z)


def embed_mobious_in_4d_sphere():
    eta, phi = np.mgrid[0:np.pi:200j, 0:2*np.pi:200j]
    mx = (np.sin(eta)*np.cos(phi))
    my = (np.sin(eta)*np.sin(phi))
    mz = (np.cos(eta)*np.cos(phi/2))
    mw = (np.cos(eta)*np.sin(phi/2))
    return (mx, my, mz, mw)


def stereographic(mx, my, mz, mw):
    my, mw = (mw+my)/np.sqrt(2), (mw-my)/np.sqrt(2)
    return (mx/(1-mw), my/(1-mw), mz/(1-mw))


def main():
    s4d = embed_mobious_in_4d_sphere()
    x, y, z = stereographic(*s4d)
    fig = make_subplots(rows=1, cols=2,
                        specs=[[{'type': 'surface'}, {'type': 'surface'}]])
    fig.add_trace(
        go.Surface(x=x, y=y, z=z, opacity=.9, showscale=False),
        row=1, col=1)
    for step in range(0, 200, 5):
        fig.add_trace(
                go.Scatter3d(
                    name="bundle",
                    visible=False,
                    x=x[:, step],
                    y=y[:, step],
                    z=z[:, step],
                    marker=dict(size=1, color='green')),
                row=1, col=1)
    for step in range(0, 200, 5):
        fig.add_trace(
            go.Scatter3d(
                name="section",
                visible=False,
                x=np.concatenate((x[step, :], x[199-step, :])),
                y=np.concatenate((y[step, :], y[199-step, :])),
                z=np.concatenate((z[step, :], z[199-step, :])),
                marker=dict(size=2, color='red')),
            row=1, col=1)
    sx, sy, sz = non_sudanese()
    fig.add_trace(
        go.Surface(x=sx, y=sy, z=sz, opacity=.9, showscale=False),
        row=1, col=2)
    for step in range(0, 200, 5):
        fig.add_trace(
            go.Scatter3d(
                name="bundle",
                visible=False,
                x=sx[:, step],
                y=sy[:, step],
                z=sz[:, step],
                marker=dict(size=1, color='green')),
            row=1, col=2)
    for step in range(0, 200, 5):
        fig.add_trace(
            go.Scatter3d(
                name="section",
                visible=False,
                x=np.concatenate((sx[step, :], sx[199-step, :])),
                y=np.concatenate((sy[step, :], sy[199-step, :])),
                z=np.concatenate((sz[step, :], sz[199-step, :])),
                marker=dict(size=2, color='red')),
            row=1, col=2)
    fig.data[1].visible = True
    fig.data[41].visible = True
    fig.data[82].visible = True
    fig.data[122].visible = True
    steps = []
    for i in range(1, 40):
        index = dict(
            method="update",
            args=[{"visible": [False] * len(fig.data)}],
            label="")
        index["args"][0]["visible"][0] = True
        index["args"][0]["visible"][81] = True
        index["args"][0]["visible"][i] = True
        index["args"][0]["visible"][40+i] = True
        index["args"][0]["visible"][81+i] = True
        index["args"][0]["visible"][121+i] = True
        steps.append(index)
    sliders = [dict(
        active=1,
        steps=steps)]
    fig.update_layout(
        sliders=sliders,
        showlegend=False)
    fig.show()


if __name__ == "__main__":
    main()
