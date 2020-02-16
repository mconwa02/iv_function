


def calculate_iv(df, target):
    """
    Calculates the weight of evidence and information values
    Args:
        df: pandas dataframe
        target: pandas series

    Returns: pandas series
    """
    lst = []
    for features in df.columns:
        df1 = pd.concat([df[features], target], axis=1, sort=False)
        df1.columns = ["X", "Y"]
        justmiss = df1[df1.X.isnull()]
        notmiss = df1[df1.X.notnull()]
        df2 = notmiss.groupby("X", as_index=True)
        df3 = pd.DataFrame(
            {
                "COUNT": df2["Y"].count(),
                "EVENT": df2["Y"].sum(),
                "NONEVENT": df2["Y"].count() - df2["Y"].sum()
            }
        )
        if len(justmiss.index) > 0:
            df4 = pd.DataFrame(
                {
                    "COUNT": justmiss["Y"].count(),
                    "EVENT": justmiss["Y"].sum(),
                    "NONEVENT": justmiss["Y"].count() - justmiss["Y"].sum()
                },
                index=[0]
            )
            df3 = df3.append(df4, ignore_index=True)
        df3["DIST_EVENT"] = df3["EVENT"] / df3["EVENT"].sum()
        df3["DIST_NON_EVENT"] = df3["NONEVENT"] / df3["NONEVENT"].sum()
        df3["WOE"] = np.log(df3["DIST_EVENT"] / df3["DIST_NON_EVENT"])
        df3["IV"] = (df3["DIST_EVENT"] - df3["DIST_NON_EVENT"]) * np.log(
            df3["DIST_EVENT"] / df3["DIST_NON_EVENT"]
        )

        df3["VAR_NAME"] = features

        df3 = df3[
            [
                "VAR_NAME",
                "COUNT",
                "EVENT",
                "NONEVENT",
                "DIST_EVENT",
                "DIST_NON_EVENT",
                "WOE",
                "IV",
            ]
        ]
        df3 = df3.replace([np.inf, -np.inf], 0)
        df3["IV"] = df3["IV"].sum()
        df3 = df3.reset_index(drop=True)
        lst.append(df3)
    iv_df = pd.concat(lst)
    iv = iv_df.groupby("VAR_NAME").IV.max()
    return iv