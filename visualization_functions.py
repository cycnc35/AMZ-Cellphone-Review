import pandas as pd
import plotly.graph_objs as go

def brand_counts(review_item):
    count = review_item.groupby("brand").size()
    labels = count.index
    values = count.values
    data = go.Data([go.Pie(labels = labels, values = values)])
    layout = go.Layout(title={"text":"Sales Volume", 'x':0.5, 'y':0.9, 'xanchor':'center', 'yanchor':'top'}, font={"size":20})
    figure = go.Figure(data=data, layout=layout)

    return figure

def plot_stacked_rating_hist_allbrands(review_item):
    brands = sorted(list(set(review_item["brand"])))
    scores = sorted(list(set(review_item["rating_review"])))

    freq_dict = dict()
    for brand_name in brands:
        filtered_df = review_item[review_item.brand == brand_name]
        ratings = filtered_df.groupby('rating_review').size().reset_index(name='counts')
        ratings['counts'] = ratings['counts'] / len(filtered_df)
        freq_dict[brand_name] = list(ratings['counts'])

    traces = []
    for i, s in enumerate(scores):
        trace = go.Bar(x=brands, y=[freq_dict[brand][i] for brand in brands], name=str(s))
        traces.append(trace)

    layout = go.Layout(title={'text': "Frequency histogram of all brands' ratings ",
                              'x':0.5, 'y':0.9, 'xanchor':'center', 'yanchor':'top'},
                       font={"size": 16}, barmode="stack")
    figure = go.Figure(data=traces, layout=layout)

    return figure