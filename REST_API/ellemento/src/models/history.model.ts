import {Entity, model, property, hasOne, belongsTo} from '@loopback/repository';
import {TrayMovement} from './tray-movement.model';
import {TrayWashing} from './tray-washing.model';
import {Potting} from './potting.model';
import {Transplanting} from './transplanting.model';

@model({settings: {strict: false}})
export class History extends Entity {
  @property({
    type: 'number',
    id: true,
    generated: true,
  })
  history_id?: number;

  @property({
    type: 'number',
    required: true,
  })
  batch_id: number;

  @property({
    type: 'number',
    required: true,
  })
  action_type_id: number;

  @property({
    type: 'string',
    required: true,
  })
  tray_action_table: string;
  
  @property({
    type: 'number',
    required: true,
  })
  tray_action_table_id: number;
  
  @property({
    type: 'number',
    required: true,
  })
  stage_from_id: number;

  @property({
    type: 'number',
    required: true,
  })
  stage_to_id: number;

  @property({
    type: 'date',
    required: true,
  })
  date_time_start: string;

  @property({
    type: 'date',
    required: true,
  })
  date_time_end: string;

  @property({
    type: 'number',
    required: true,
  })
  amount_transferred: number;

  @property({
    type: 'number',
    required: true,
  })
  error_type_id: number;

  @property({
    type: 'string',
  })
  comment?: string;

  @property({
    type: 'number',
  })
  batchId?: number;


  @property({
    type: 'number',
  })
  errorTypeId?: number;


  // Define well-known properties here

  // Indexer property to allow additional data
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  [prop: string]: any;

  constructor(data?: Partial<History>) {
    super(data);
  }
}

export interface HistoryRelations {
  // describe navigational properties here
}

export type HistoryWithRelations = History & HistoryRelations;
