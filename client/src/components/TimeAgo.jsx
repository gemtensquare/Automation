import dayjs from 'dayjs';
import relativeTime from 'dayjs/plugin/relativeTime';

dayjs.extend(relativeTime);

const TimeAgo = ({ isoDate }) => {
  return <span>{dayjs(isoDate).fromNow()}</span>;
};

export default TimeAgo;